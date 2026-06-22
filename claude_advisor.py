"""
claude_advisor.py — Claude-powered plain-language explanations.

SEAD 3 / Whole-Person Concept framing applies throughout:
  - Claude EXPLAINS what adjudicators are trained to evaluate.
  - Claude NEVER predicts, scores, or determines clearance outcomes.
  - All content is sourced from public SEAD 4 / Adjudicative Desk Reference.
"""
from __future__ import annotations

import json
import os

import anthropic

from config import MODEL
from guidelines import GUIDELINES_BY_CODE

_SYSTEM_PROMPT = """\
You are a security clearance education assistant. Your role is to explain the U.S. \
federal security clearance adjudicative guidelines in plain language so that clearance \
candidates can understand the process. You NEVER predict whether someone will receive a \
clearance. You NEVER score, assess, or make determinations about individuals. You \
NEVER offer legal advice. You explain what the guidelines cover and what topics \
adjudicators are trained to explore — nothing more.

All of your explanations are grounded in publicly available government documents: \
Security Executive Agent Directive 4 (SEAD 4) and the Adjudicative Desk Reference (ADR) \
published by the Defense Counterintelligence and Security Agency (DCSA).

When describing adjudicative concerns, always frame them as "adjudicators are trained to \
consider" or "the guideline addresses" — not as "you are at risk" or "this will affect you."

Respond in plain, clear English appropriate for someone unfamiliar with security clearance \
terminology. Avoid jargon. When you must use a term of art (e.g., "whole-person concept"), \
briefly define it.
"""


def _client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable is not set.")
    return anthropic.Anthropic(api_key=api_key)


def generate_briefings(
    guidelines_selected: list[str],
    clearance_level: str,
    context_notes: str = "",
) -> str:
    """
    Generate plain-language briefings for each selected guideline.

    Returns a JSON string mapping guideline code → briefing text.
    Raises RuntimeError if ANTHROPIC_API_KEY is not set.
    """
    client = _client()
    guidelines_detail = []
    for code in guidelines_selected:
        g = GUIDELINES_BY_CODE.get(code.upper())
        if g:
            guidelines_detail.append(
                f"Guideline {g['code']}: {g['name']}\n"
                f"What it covers: {g['what_it_covers']}\n"
                f"Key concerns adjudicators evaluate:\n"
                + "\n".join(f"  - {c}" for c in g["concerns"])
            )

    user_message = (
        f"A candidate is preparing to understand the security clearance process for a "
        f"{clearance_level} clearance. They want plain-language explanations of the "
        f"following adjudicative guidelines:\n\n"
        + "\n\n".join(guidelines_detail)
        + (f"\n\nAdditional context provided by the candidate: {context_notes}" if context_notes else "")
        + "\n\nFor each guideline, write a clear, educational explanation (3-5 paragraphs) that:\n"
        "1. Explains what the guideline addresses and WHY it matters to national security\n"
        "2. Describes what kinds of situations or history an adjudicator is trained to explore\n"
        "3. Explains what the Adjudicative Desk Reference says about mitigating factors\n"
        "4. Emphasizes the whole-person concept and that context matters\n\n"
        "IMPORTANT: Do NOT predict outcomes. Do NOT assess the candidate. Frame everything "
        "as educational information about the process.\n\n"
        "Respond with a JSON object where each key is the guideline letter code and the "
        'value is the briefing text. Example: {"B": "...", "F": "..."}'
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    raw = response.content[0].text.strip()
    raw = _strip_fences(raw)

    # Validate it's valid JSON before returning
    parsed = json.loads(raw)
    return json.dumps(parsed)


def generate_interview_prep(
    guidelines_selected: list[str],
    clearance_level: str,
    context_notes: str = "",
) -> str:
    """
    Generate a Subject Interview preparation guide for selected guidelines.

    Returns a markdown-formatted string.
    Raises RuntimeError if ANTHROPIC_API_KEY is not set.
    """
    client = _client()
    guidelines_summary = []
    for code in guidelines_selected:
        g = GUIDELINES_BY_CODE.get(code.upper())
        if g:
            topics = "\n".join(f"  - {t}" for t in g["interview_topics"])
            guidelines_summary.append(
                f"Guideline {g['code']} ({g['name']}):\n{topics}"
            )

    user_message = (
        f"A candidate preparing for a {clearance_level} Subject Interview wants to "
        f"understand what topics are likely to come up based on the following adjudicative "
        f"guidelines they have selected:\n\n"
        + "\n\n".join(guidelines_summary)
        + (f"\n\nAdditional context: {context_notes}" if context_notes else "")
        + "\n\nWrite a practical Subject Interview preparation guide that:\n"
        "1. Explains what a Subject Interview is and how it works\n"
        "2. For each guideline, lists the types of questions an investigator is trained "
        "to ask (framed as 'investigators may ask...')\n"
        "3. Explains the importance of being thorough, honest, and forthright\n"
        "4. Describes what to expect from the interview process\n"
        "5. Recommends consulting a security clearance attorney for legal advice\n\n"
        "IMPORTANT: This is educational preparation — NOT legal advice. Do NOT predict "
        "outcomes. Frame everything as 'investigators are trained to explore' or "
        "'the interview may cover' — never as 'you will be asked' or 'this is a problem.'\n\n"
        "Format your response in markdown with clear headers for each section."
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=3000,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    return response.content[0].text.strip()


def _strip_fences(text: str) -> str:
    import re
    text = re.sub(r"^```(?:json)?\s*\n?", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n?```\s*$", "", text, flags=re.MULTILINE)
    return text.strip()
