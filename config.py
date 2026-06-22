"""config.py — Security Clearance Readiness Advisor configuration."""
import os

DEMO_MODE = os.getenv("DEMO_MODE", "True") == "True"
MODEL = "claude-haiku-4-5-20251001"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./clearance_advisor.db")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

CLEARANCE_LEVELS = [
    "SECRET",
    "TOP SECRET",
    "TOP SECRET / SCI",
]

DISCLAIMER = (
    "This tool is for educational purposes only. It explains publicly available "
    "adjudicative guidelines to help you understand the security clearance process. "
    "It does NOT predict whether you will receive a clearance, does NOT constitute "
    "legal advice, and does NOT substitute for consultation with a security clearance "
    "attorney. Clearance decisions are made by trained adjudicators using a holistic "
    "whole-person evaluation. All content is sourced from publicly available government "
    "documents (SEAD 4, Adjudicative Desk Reference)."
)

PROCESS_NOTE = (
    "Adjudicators apply the Whole Person Concept — no single factor automatically "
    "disqualifies an applicant. Context, recency, frequency, and demonstrated "
    "rehabilitation all matter. The guidelines below describe what adjudicators are "
    "trained to evaluate, not a checklist of disqualifying conditions."
)
