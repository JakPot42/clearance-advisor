"""Tests for claude_advisor.py — mocked Anthropic calls."""
import json
from unittest.mock import MagicMock, patch

import pytest


class TestGenerateBriefings:
    def _mock_response(self, text: str):
        msg = MagicMock()
        msg.content = [MagicMock(text=text)]
        return msg

    def test_returns_json_string(self):
        payload = json.dumps({"B": "Guideline B briefing text.", "F": "Guideline F briefing text."})
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(payload)
            mock_client_fn.return_value = client

            import claude_advisor
            result = claude_advisor.generate_briefings(["B", "F"], "SECRET")

        parsed = json.loads(result)
        assert "B" in parsed
        assert "F" in parsed

    def test_strips_markdown_fences(self):
        payload = '```json\n{"E": "Guideline E explanation."}\n```'
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(payload)
            mock_client_fn.return_value = client

            import claude_advisor
            result = claude_advisor.generate_briefings(["E"], "SECRET")

        parsed = json.loads(result)
        assert parsed["E"] == "Guideline E explanation."

    def test_includes_clearance_level_in_prompt(self):
        payload = json.dumps({"G": "Guideline G text."})
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(payload)
            mock_client_fn.return_value = client

            import claude_advisor
            claude_advisor.generate_briefings(["G"], "TOP SECRET")

        call_args = client.messages.create.call_args
        messages = call_args[1]["messages"]
        assert "TOP SECRET" in messages[0]["content"]

    def test_includes_context_notes_when_provided(self):
        payload = json.dumps({"H": "Drug guideline text."})
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(payload)
            mock_client_fn.return_value = client

            import claude_advisor
            claude_advisor.generate_briefings(["H"], "SECRET", "Student loan debt")

        call_args = client.messages.create.call_args
        messages = call_args[1]["messages"]
        assert "Student loan debt" in messages[0]["content"]

    def test_skips_unknown_codes(self):
        payload = json.dumps({"B": "B text."})
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(payload)
            mock_client_fn.return_value = client

            import claude_advisor
            result = claude_advisor.generate_briefings(["B", "Z"], "SECRET")

        call_args = client.messages.create.call_args
        messages = call_args[1]["messages"]
        assert "Guideline Z" not in messages[0]["content"]

    def test_raises_without_api_key(self):
        with patch("claude_advisor.os.getenv", return_value=""):
            import claude_advisor
            with pytest.raises(RuntimeError, match="ANTHROPIC_API_KEY"):
                claude_advisor.generate_briefings(["B"], "SECRET")


class TestGenerateInterviewPrep:
    def _mock_response(self, text: str):
        msg = MagicMock()
        msg.content = [MagicMock(text=text)]
        return msg

    def test_returns_markdown_string(self):
        markdown = "# Interview Prep\n\n## What to expect\n\nInvestigators may ask..."
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(markdown)
            mock_client_fn.return_value = client

            import claude_advisor
            result = claude_advisor.generate_interview_prep(["B", "F"], "SECRET")

        assert isinstance(result, str)
        assert "Interview Prep" in result

    def test_includes_guideline_names_in_prompt(self):
        markdown = "# Interview Prep"
        with patch("claude_advisor._client") as mock_client_fn:
            client = MagicMock()
            client.messages.create.return_value = self._mock_response(markdown)
            mock_client_fn.return_value = client

            import claude_advisor
            claude_advisor.generate_interview_prep(["F"], "SECRET")

        call_args = client.messages.create.call_args
        messages = call_args[1]["messages"]
        assert "Financial Considerations" in messages[0]["content"]

    def test_raises_without_api_key(self):
        with patch("claude_advisor.os.getenv", return_value=""):
            import claude_advisor
            with pytest.raises(RuntimeError, match="ANTHROPIC_API_KEY"):
                claude_advisor.generate_interview_prep(["E"], "SECRET")


class TestStripFences:
    def test_strips_json_fence(self):
        import claude_advisor
        raw = '```json\n{"a": 1}\n```'
        assert claude_advisor._strip_fences(raw) == '{"a": 1}'

    def test_strips_plain_fence(self):
        import claude_advisor
        raw = '```\n{"b": 2}\n```'
        assert claude_advisor._strip_fences(raw) == '{"b": 2}'

    def test_no_fence_passthrough(self):
        import claude_advisor
        raw = '{"c": 3}'
        assert claude_advisor._strip_fences(raw) == '{"c": 3}'
