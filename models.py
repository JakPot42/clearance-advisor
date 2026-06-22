"""models.py — ORM models for the Security Clearance Readiness Advisor."""
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_name = Column(String(200), nullable=False)
    clearance_level = Column(String(50), nullable=False)
    guidelines_selected = Column(Text, nullable=False)  # JSON list: ["B", "F", "H"]
    context_notes = Column(Text, default="")
    claude_briefings = Column(Text, default="")        # Claude plain-language briefings
    interview_prep = Column(Text, default="")          # Claude interview prep guide
    is_demo = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))
