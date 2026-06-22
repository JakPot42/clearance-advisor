"""Tests for database.py and models.py."""
import json
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from models import Session as SessionModel


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    Sess = sessionmaker(bind=engine)
    session = Sess()
    yield session
    session.close()
    engine.dispose()


class TestSessionModel:
    def test_create_session(self, db):
        s = SessionModel(
            session_name="Test Session",
            clearance_level="SECRET",
            guidelines_selected=json.dumps(["B", "F"]),
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        assert s.id is not None
        assert s.session_name == "Test Session"

    def test_default_is_demo_false(self, db):
        s = SessionModel(
            session_name="Live Session",
            clearance_level="TOP SECRET",
            guidelines_selected=json.dumps(["E"]),
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        assert s.is_demo is False

    def test_created_at_auto_set(self, db):
        s = SessionModel(
            session_name="Timed",
            clearance_level="SECRET",
            guidelines_selected=json.dumps(["G"]),
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        assert s.created_at is not None

    def test_claude_briefings_json_roundtrip(self, db):
        briefings = {"B": "Briefing for guideline B.", "F": "Briefing for guideline F."}
        s = SessionModel(
            session_name="With Briefings",
            clearance_level="SECRET",
            guidelines_selected=json.dumps(["B", "F"]),
            claude_briefings=json.dumps(briefings),
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        loaded = json.loads(s.claude_briefings)
        assert loaded["B"] == "Briefing for guideline B."

    def test_interview_prep_default_empty(self, db):
        s = SessionModel(
            session_name="No Prep",
            clearance_level="SECRET",
            guidelines_selected=json.dumps(["A"]),
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        assert s.interview_prep == ""

    def test_multiple_sessions(self, db):
        for i in range(5):
            db.add(SessionModel(
                session_name=f"Session {i}",
                clearance_level="SECRET",
                guidelines_selected=json.dumps(["E"]),
            ))
        db.commit()
        count = db.query(SessionModel).count()
        assert count == 5

    def test_context_notes_optional(self, db):
        s = SessionModel(
            session_name="No Notes",
            clearance_level="SECRET",
            guidelines_selected=json.dumps(["J"]),
            context_notes="",
        )
        db.add(s)
        db.commit()
        db.refresh(s)
        assert s.context_notes == ""


class TestSeedData:
    def test_seed_creates_three_sessions(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        count = db.query(SessionModel).count()
        assert count == 3

    def test_seed_idempotent(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        seed_demo_sessions(db)
        count = db.query(SessionModel).count()
        assert count == 3

    def test_seed_demo_flags_set(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        demos = db.query(SessionModel).filter_by(is_demo=True).count()
        assert demos == 3

    def test_seed_sessions_have_briefings(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        sessions = db.query(SessionModel).all()
        for s in sessions:
            assert s.claude_briefings
            briefings = json.loads(s.claude_briefings)
            assert len(briefings) > 0

    def test_seed_sessions_have_interview_prep(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        sessions = db.query(SessionModel).all()
        for s in sessions:
            assert s.interview_prep
            assert len(s.interview_prep) > 100

    def test_seed_session_clearance_levels(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        levels = {s.clearance_level for s in db.query(SessionModel).all()}
        assert "SECRET" in levels
        assert "TOP SECRET / SCI" in levels

    def test_seed_guidelines_valid_json(self, db):
        from seed_data import seed_demo_sessions
        seed_demo_sessions(db)
        for s in db.query(SessionModel).all():
            codes = json.loads(s.guidelines_selected)
            assert isinstance(codes, list)
            assert all(c in "ABCDEFGHIJKLM" for c in codes)
