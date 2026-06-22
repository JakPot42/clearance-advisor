"""Tests for main.py FastAPI routes."""
import json
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app
from models import Session as SessionModel
from seed_data import DEMO_SESSIONS


@pytest.fixture(autouse=True)
def test_db():
    # StaticPool reuses one connection so all sessions see the same in-memory DB.
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    TestSession = sessionmaker(bind=engine)

    def override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # Seed demo sessions
    db = TestSession()
    from seed_data import seed_demo_sessions
    seed_demo_sessions(db)
    db.close()

    yield

    app.dependency_overrides.clear()
    engine.dispose()


@pytest.fixture
def client():
    return TestClient(app)


class TestHomeRoute:
    def test_home_returns_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_home_contains_demo_sessions(self, client):
        resp = client.get("/")
        assert "Entry-Level SECRET" in resp.text

    def test_home_contains_guidelines_grid(self, client):
        resp = client.get("/")
        assert "Guidelines" in resp.text


class TestGuidelinesRoutes:
    def test_guidelines_list_200(self, client):
        resp = client.get("/guidelines")
        assert resp.status_code == 200

    def test_guidelines_list_contains_all_codes(self, client):
        resp = client.get("/guidelines")
        for code in "ABCDEFGHIJKLM":
            assert f">{code}<" in resp.text or f"/{code}" in resp.text

    def test_guideline_detail_200(self, client):
        resp = client.get("/guidelines/B")
        assert resp.status_code == 200

    def test_guideline_detail_contains_name(self, client):
        resp = client.get("/guidelines/B")
        assert "Foreign Influence" in resp.text

    def test_guideline_detail_lowercase_code(self, client):
        resp = client.get("/guidelines/b")
        assert resp.status_code == 200

    def test_guideline_detail_unknown_code_404(self, client):
        resp = client.get("/guidelines/Z")
        assert resp.status_code == 404

    def test_guideline_detail_contains_concerns(self, client):
        resp = client.get("/guidelines/F")
        assert "Financial" in resp.text

    def test_guideline_detail_no_prediction_language(self, client):
        resp = client.get("/guidelines/H")
        # The disclaimer correctly says "does NOT predict whether you will receive" —
        # that's fine. Check for actual affirmative prediction language instead.
        assert "you will pass" not in resp.text.lower()
        assert "you will fail" not in resp.text.lower()
        assert "you will be denied" not in resp.text.lower()
        assert "you will be approved" not in resp.text.lower()


class TestSessionRoutes:
    def test_session_new_form_200(self, client):
        resp = client.get("/session/new")
        assert resp.status_code == 200

    def test_session_new_form_has_checkboxes(self, client):
        resp = client.get("/session/new")
        assert 'name="guidelines_selected"' in resp.text

    def test_session_new_form_has_clearance_levels(self, client):
        resp = client.get("/session/new")
        assert "SECRET" in resp.text

    def test_session_view_demo_200(self, client):
        resp = client.get("/session/1")
        assert resp.status_code == 200

    def test_session_view_contains_session_name(self, client):
        resp = client.get("/session/1")
        assert "Entry-Level SECRET" in resp.text

    def test_session_view_404_unknown(self, client):
        resp = client.get("/session/9999")
        assert resp.status_code == 404

    def test_session_view_has_briefings(self, client):
        resp = client.get("/session/1")
        # Demo session 1 has briefings for E, F, H
        assert "Personal Conduct" in resp.text or "Guideline E" in resp.text

    def test_session_view_has_interview_prep(self, client):
        resp = client.get("/session/1")
        # Demo session 1 has pre-baked interview prep
        assert "Subject Interview" in resp.text

    def test_session_report_200(self, client):
        resp = client.get("/session/1/report")
        assert resp.status_code == 200

    def test_session_report_contains_disclaimer(self, client):
        resp = client.get("/session/1/report")
        assert "Educational Tool Only" in resp.text or "educational purposes" in resp.text.lower()

    def test_create_session_demo_mode(self, client):
        data = {
            "session_name": "Test Create",
            "clearance_level": "SECRET",
            "guidelines_selected": ["B"],
            "context_notes": "",
        }
        with patch("config.DEMO_MODE", True):
            resp = client.post("/session/new", data=data)
        # Should redirect to new session
        assert resp.status_code in (200, 303, 302)

    def test_create_session_invalid_clearance_level(self, client):
        data = {
            "session_name": "Bad Level",
            "clearance_level": "ULTRA_SECRET",
            "guidelines_selected": ["B"],
        }
        resp = client.post("/session/new", data=data)
        assert resp.status_code in (400, 422)

    def test_create_session_no_guidelines(self, client):
        data = {
            "session_name": "No Guidelines",
            "clearance_level": "SECRET",
            "guidelines_selected": ["Z"],  # invalid code
        }
        resp = client.post("/session/new", data=data)
        assert resp.status_code in (400, 422)


class TestInterviewPrepRoute:
    def test_generate_prep_redirects(self, client):
        resp = client.post("/session/1/interview-prep", follow_redirects=False)
        # Demo mode: generates placeholder and redirects
        assert resp.status_code in (302, 303, 200)

    def test_generate_prep_unknown_session_404(self, client):
        resp = client.post("/session/9999/interview-prep")
        assert resp.status_code == 404


class TestStatsRoute:
    def test_stats_200(self, client):
        resp = client.get("/api/stats")
        assert resp.status_code == 200

    def test_stats_has_session_count(self, client):
        resp = client.get("/api/stats")
        data = resp.json()
        assert "total_sessions" in data
        assert data["total_sessions"] >= 3

    def test_stats_has_guidelines_count(self, client):
        resp = client.get("/api/stats")
        data = resp.json()
        assert data["guidelines_count"] == 13

    def test_stats_has_demo_mode(self, client):
        resp = client.get("/api/stats")
        data = resp.json()
        assert "demo_mode" in data
