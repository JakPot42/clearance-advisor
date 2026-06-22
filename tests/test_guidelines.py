"""Tests for guidelines.py — content correctness and lookup functions."""
import pytest
from guidelines import GUIDELINES, GUIDELINES_BY_CODE, all_codes, get_guideline


class TestGuidelinesStructure:
    def test_exactly_13_guidelines(self):
        assert len(GUIDELINES) == 13

    def test_codes_a_through_m(self):
        codes = {g["code"] for g in GUIDELINES}
        assert codes == {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"}

    def test_each_guideline_has_required_fields(self):
        required = {"code", "name", "short", "what_it_covers", "concerns",
                    "disqualifying", "mitigating", "adr_section", "interview_topics"}
        for g in GUIDELINES:
            missing = required - g.keys()
            assert not missing, f"Guideline {g['code']} missing: {missing}"

    def test_concerns_not_empty(self):
        for g in GUIDELINES:
            assert len(g["concerns"]) >= 2, f"Guideline {g['code']} needs at least 2 concerns"

    def test_disqualifying_not_empty(self):
        for g in GUIDELINES:
            assert len(g["disqualifying"]) >= 1

    def test_mitigating_not_empty(self):
        for g in GUIDELINES:
            assert len(g["mitigating"]) >= 1

    def test_interview_topics_not_empty(self):
        for g in GUIDELINES:
            assert len(g["interview_topics"]) >= 1

    def test_no_prediction_language_in_content(self):
        forbidden = ["will receive", "will be denied", "you will pass", "you will fail",
                     "your chances", "predict"]
        for g in GUIDELINES:
            for field in ["what_it_covers", "short"]:
                text = g[field].lower()
                for phrase in forbidden:
                    assert phrase not in text, (
                        f"Guideline {g['code']}.{field} contains forbidden phrase: {phrase!r}"
                    )


class TestGuidelineLookup:
    def test_get_guideline_by_code(self):
        g = get_guideline("B")
        assert g is not None
        assert g["code"] == "B"
        assert "Foreign Influence" in g["name"]

    def test_get_guideline_case_insensitive(self):
        assert get_guideline("b") is not None
        assert get_guideline("b")["code"] == "B"

    def test_get_guideline_unknown_code_returns_none(self):
        assert get_guideline("Z") is None
        assert get_guideline("") is None

    def test_guidelines_by_code_dict(self):
        assert len(GUIDELINES_BY_CODE) == 13
        for code in "ABCDEFGHIJKLM":
            assert code in GUIDELINES_BY_CODE

    def test_all_codes_returns_13(self):
        codes = all_codes()
        assert len(codes) == 13

    def test_all_codes_in_order(self):
        codes = all_codes()
        assert codes == list("ABCDEFGHIJKLM")


class TestGuidelineContent:
    def test_guideline_f_mentions_financial(self):
        g = get_guideline("F")
        assert "financial" in g["what_it_covers"].lower()

    def test_guideline_b_mentions_foreign(self):
        g = get_guideline("B")
        assert "foreign" in g["what_it_covers"].lower()

    def test_guideline_h_mentions_marijuana(self):
        g = get_guideline("H")
        all_text = " ".join(g["concerns"] + g["disqualifying"] + [g["what_it_covers"]])
        assert "marijuana" in all_text.lower()

    def test_guideline_i_encourages_treatment(self):
        g = get_guideline("I")
        all_mitigating = " ".join(g["mitigating"]).lower()
        assert "treatment" in all_mitigating

    def test_guideline_e_mentions_sf86(self):
        g = get_guideline("E")
        all_text = " ".join(g["concerns"] + [g["what_it_covers"]]).lower()
        assert "sf-86" in all_text or "sf86" in all_text

    def test_guideline_d_notes_orientation_not_concern(self):
        g = get_guideline("D")
        all_text = " ".join([g["what_it_covers"]] + g["interview_topics"]).lower()
        assert "sexual orientation" in all_text

    def test_guideline_c_distinguishes_passive_dual_citizenship(self):
        g = get_guideline("C")
        assert "dual" in g["what_it_covers"].lower()

    def test_adr_section_format(self):
        for g in GUIDELINES:
            assert g["adr_section"].startswith("Guideline ")
