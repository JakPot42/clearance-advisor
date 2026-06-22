# Security Clearance Readiness Advisor

An educational web application that explains the 13 adjudicative guidelines from the
publicly available **Adjudicative Desk Reference (ADR)** — helping clearance candidates
understand the process and prepare for Subject Interviews.

**Live demo:** https://clearance-advisor.onrender.com

---

## What This Tool Does

- **Explains** each of the 13 SEAD 4 adjudicative guidelines in plain language
- **Describes** what adjudicators are trained to evaluate under each guideline
- **Identifies** mitigating factors the ADR associates with each area of concern
- **Prepares** candidates for the Subject Interview by listing topics investigators may explore
- **Never predicts** whether a candidate will receive a clearance — that is adjudicator territory

## What This Tool Does NOT Do

- Predict clearance outcomes
- Score or assess individuals
- Provide legal advice
- Access any government database or clearance system
- Substitute for consultation with a security clearance attorney

---

## The 13 Adjudicative Guidelines (SEAD 4)

| Code | Guideline |
|------|-----------|
| A | Allegiance to the United States |
| B | Foreign Influence |
| C | Foreign Preference |
| D | Sexual Behavior |
| E | Personal Conduct |
| F | Financial Considerations |
| G | Alcohol Consumption |
| H | Drug Involvement and Substance Misuse |
| I | Psychological Conditions |
| J | Criminal Conduct |
| K | Handling Protected Information |
| L | Outside Activities |
| M | Use of Information Technology Systems |

**Source:** Security Executive Agent Directive 4 (SEAD 4), effective June 8, 2017.
Adjudicative Desk Reference (ADR), Defense Counterintelligence and Security Agency (DCSA).

---

## Tech Stack

- **Backend:** FastAPI + Jinja2
- **Database:** SQLite + SQLAlchemy 2.0
- **AI:** Claude Haiku (`claude-haiku-4-5-20251001`) for plain-language briefings
- **Deployment:** Render (free tier)

## Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The app auto-seeds three demo sessions on startup. Set `ANTHROPIC_API_KEY` and
`DEMO_MODE=False` to enable live Claude-generated briefings.

## Running Tests

```bash
pytest tests/ -v
```

78 tests, all passing. No real API calls — Claude is fully mocked in tests.

---

## Architecture

```
guidelines.py     ← All 13 guideline definitions (content layer)
claude_advisor.py ← Claude briefing + interview prep generation
seed_data.py      ← 3 pre-baked demo sessions with full Claude responses
main.py           ← FastAPI routes
database.py       ← SQLAlchemy engine + session factory
models.py         ← Session ORM model
config.py         ← App configuration + disclaimer text
```

**SEAD 3 framing applies throughout:** Claude explains and educates; Claude never
makes determinations about individuals. Every briefing is framed as "adjudicators
are trained to consider" — never as a prediction or score.

---

## Honest Limitations

- Content is drawn from public ADR excerpts — not a complete reproduction of the ADR
- Claude briefings are educational summaries, not legal advice
- Candidates with complex situations should consult a cleared attorney
- Clearance determinations involve the full SF-86 investigation, reference checks,
  and interviews — no tool can replicate that holistic process
