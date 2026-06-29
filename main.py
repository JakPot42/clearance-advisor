"""
main.py — Security Clearance Readiness Advisor (FastAPI application).

Educational tool only. All content sourced from SEAD 4 / Adjudicative Desk Reference.
Claude EXPLAINS guidelines. Claude NEVER predicts clearance outcomes.
"""
from __future__ import annotations

import json
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from config import CLEARANCE_LEVELS, DEMO_MODE, DISCLAIMER, PROCESS_NOTE
from database import get_db, init_db
from guidelines import GUIDELINES, get_guideline
from models import Session as SessionModel
from seed_data import seed_demo_sessions


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    db = next(get_db())
    try:
        seed_demo_sessions(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="Security Clearance Readiness Advisor",
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.filters["fromjson"] = json.loads


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    sessions = db.query(SessionModel).order_by(SessionModel.created_at.desc()).all()
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "sessions": sessions,
            "guidelines": GUIDELINES,
            "demo_mode": DEMO_MODE,
            "disclaimer": DISCLAIMER,
        },
    )


# ---------------------------------------------------------------------------
# Guidelines
# ---------------------------------------------------------------------------

@app.get("/guidelines", response_class=HTMLResponse)
async def guidelines_list(request: Request):
    return templates.TemplateResponse(
        request,
        "guidelines.html",
        {
            "guidelines": GUIDELINES,
            "process_note": PROCESS_NOTE,
            "disclaimer": DISCLAIMER,
        },
    )


@app.get("/guidelines/{code}", response_class=HTMLResponse)
async def guideline_detail(request: Request, code: str):
    g = get_guideline(code)
    if not g:
        raise HTTPException(status_code=404, detail=f"Guideline {code!r} not found")
    return templates.TemplateResponse(
        request,
        "guideline_detail.html",
        {
            "guideline": g,
            "disclaimer": DISCLAIMER,
        },
    )


# ---------------------------------------------------------------------------
# Sessions
# ---------------------------------------------------------------------------

@app.get("/session/new", response_class=HTMLResponse)
async def session_new_form(request: Request):
    return templates.TemplateResponse(
        request,
        "session_new.html",
        {
            "guidelines": GUIDELINES,
            "clearance_levels": CLEARANCE_LEVELS,
            "demo_mode": DEMO_MODE,
            "disclaimer": DISCLAIMER,
        },
    )


_MAX_CONTEXT_CHARS = 2_000

@app.post("/session/new")
async def session_new_submit(
    request: Request,
    session_name: str = Form(...),
    clearance_level: str = Form(...),
    guidelines_selected: list[str] = Form(...),
    context_notes: str = Form(""),
    db: Session = Depends(get_db),
):
    if clearance_level not in CLEARANCE_LEVELS:
        raise HTTPException(status_code=400, detail="Invalid clearance level")

    if len(context_notes) > _MAX_CONTEXT_CHARS:
        raise HTTPException(
            status_code=422,
            detail=f"Context notes too long ({len(context_notes):,} chars). Maximum is {_MAX_CONTEXT_CHARS:,} characters."
        )

    valid_codes = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"}
    codes = [c for c in guidelines_selected if c in valid_codes]
    if not codes:
        raise HTTPException(status_code=400, detail="At least one guideline must be selected")

    briefings_json = ""
    if DEMO_MODE:
        briefings_json = json.dumps({
            code: (
                f"[DEMO MODE] Briefing for Guideline {code}: "
                f"{get_guideline(code)['name']}. "
                "Set ANTHROPIC_API_KEY and DEMO_MODE=False to generate a real briefing."
            )
            for code in codes
        })
    else:
        import claude_advisor
        briefings_json = claude_advisor.generate_briefings(
            codes, clearance_level, context_notes
        )

    new_session = SessionModel(
        session_name=session_name.strip(),
        clearance_level=clearance_level,
        guidelines_selected=json.dumps(codes),
        context_notes=context_notes.strip(),
        claude_briefings=briefings_json,
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return RedirectResponse(url=f"/session/{new_session.id}", status_code=303)


@app.get("/session/{session_id}", response_class=HTMLResponse)
async def session_view(request: Request, session_id: int, db: Session = Depends(get_db)):
    session = db.query(SessionModel).filter_by(id=session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    codes = json.loads(session.guidelines_selected)
    briefings = json.loads(session.claude_briefings) if session.claude_briefings else {}
    guidelines_data = [get_guideline(c) for c in codes if get_guideline(c)]

    return templates.TemplateResponse(
        request,
        "session.html",
        {
            "session": session,
            "codes": codes,
            "briefings": briefings,
            "guidelines_data": guidelines_data,
            "has_interview_prep": bool(session.interview_prep),
            "demo_mode": DEMO_MODE,
            "disclaimer": DISCLAIMER,
        },
    )


@app.post("/session/{session_id}/interview-prep")
async def generate_interview_prep(
    request: Request,
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.query(SessionModel).filter_by(id=session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    codes = json.loads(session.guidelines_selected)

    if DEMO_MODE:
        prep = (
            "**[DEMO MODE] Interview Preparation Guide**\n\n"
            "This is a placeholder. Set ANTHROPIC_API_KEY and DEMO_MODE=False "
            "to generate a real interview preparation guide.\n\n"
            "In live mode, this guide will explain what a Subject Interview is, "
            "list the types of questions investigators are trained to ask for each "
            "selected guideline, and provide practical advice for being forthright "
            "and complete during the interview."
        )
    else:
        import claude_advisor
        prep = claude_advisor.generate_interview_prep(
            codes, session.clearance_level, session.context_notes
        )

    session.interview_prep = prep
    db.commit()

    return RedirectResponse(url=f"/session/{session_id}", status_code=303)


@app.get("/session/{session_id}/report", response_class=HTMLResponse)
async def session_report(
    request: Request,
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.query(SessionModel).filter_by(id=session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    codes = json.loads(session.guidelines_selected)
    briefings = json.loads(session.claude_briefings) if session.claude_briefings else {}
    guidelines_data = [get_guideline(c) for c in codes if get_guideline(c)]

    return templates.TemplateResponse(
        request,
        "report.html",
        {
            "session": session,
            "codes": codes,
            "briefings": briefings,
            "guidelines_data": guidelines_data,
            "disclaimer": DISCLAIMER,
        },
    )


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/api/stats")
async def stats(db: Session = Depends(get_db)):
    total = db.query(SessionModel).count()
    demos = db.query(SessionModel).filter_by(is_demo=True).count()
    return {
        "total_sessions": total,
        "demo_sessions": demos,
        "demo_mode": DEMO_MODE,
        "guidelines_count": 13,
    }
