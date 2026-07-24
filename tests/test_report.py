import json

from compliance_assistant.report import (
    save_json_report,
    save_markdown_report,
)


def make_report_item(
    status="covered",
    requirement_ids=None,
    evidence_ids=None,
    evidence_types=None,
    confidence_levels=None,
    missing_evidence=False,
):
    return {
        "obligation_id": "OBL-001",
        "obligation_title": "Protect personal data",
        "status": status,
        "risk_level": "High",
        "priority": "Low",
        "recommendation": "Continue monitoring compliance.",
        "requirement_ids": (
            ["REQ-001"]
            if requirement_ids is None
            else requirement_ids
        ),
        "evidence_ids": (
            ["EVID-001"]
            if evidence_ids is None
            else evidence_ids
        ),
        "evidence_types": (
            ["Test Report"]
            if evidence_types is None
            else evidence_types
        ),
        "confidence_levels": (
            ["High"]
            if confidence_levels is None
            else confidence_levels
        ),
        "missing_evidence": missing_evidence,
    }


def test_save_json_report_creates_valid_json_file(tmp_path):
    report = [make_report_item()]
    output_path = tmp_path / "output" / "report.json"

    save_json_report(report, output_path)

    assert output_path.exists()

    saved_data = json.loads(
        output_path.read_text(encoding="utf-8")
    )

    assert saved_data == report
    assert saved_data[0]["obligation_id"] == "OBL-001"
    assert saved_data[0]["status"] == "covered"


def test_save_markdown_report_for_covered_obligation(tmp_path):
    report = [make_report_item()]
    output_path = tmp_path / "output" / "report.md"

    save_markdown_report(report, output_path)

    assert output_path.exists()

    content = output_path.read_text(encoding="utf-8")

    assert "# Continuous Compliance Traceability Report" in content
    assert "OBL-001" in content
    assert "Protect personal data" in content
    assert "- **Status:** covered" in content
    assert "- **Risk level:** High" in content
    assert "- **Priority:** Low" in content
    assert "- **Requirements:** REQ-001" in content
    assert "- **Evidence:** EVID-001" in content
    assert "- **Evidence types:** Test Report" in content
    assert "- **Confidence level:** High" in content
    assert "- **Missing evidence:** No" in content
    assert (
        "supporting engineering evidence has been recorded"
        in content
    )


def test_save_markdown_report_for_partially_covered_obligation(
    tmp_path,
):
    report_item = make_report_item(
        status="partially covered",
        evidence_ids=[],
        evidence_types=[],
        confidence_levels=[],
        missing_evidence=True,
    )

    report_item["priority"] = "High"
    report_item["recommendation"] = (
        "Immediate evidence collection required."
    )

    output_path = tmp_path / "report.md"

    save_markdown_report([report_item], output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "- **Status:** partially covered" in content
    assert "- **Requirements:** REQ-001" in content
    assert "- **Evidence:** None" in content
    assert "- **Evidence types:** None" in content
    assert "- **Confidence level:** None" in content
    assert "- **Missing evidence:** Yes" in content
    assert (
        "but no supporting engineering evidence has been recorded"
        in content
    )
    assert (
        "- **Recommendation:** "
        "Immediate evidence collection required."
        in content
    )


def test_save_markdown_report_for_uncovered_obligation(tmp_path):
    report_item = make_report_item(
        status="uncovered",
        requirement_ids=[],
        evidence_ids=[],
        evidence_types=[],
        confidence_levels=[],
        missing_evidence=True,
    )

    report_item["priority"] = "Medium"
    report_item["recommendation"] = (
        "Compliance work should begin soon."
    )

    output_path = tmp_path / "report.md"

    save_markdown_report([report_item], output_path)

    content = output_path.read_text(encoding="utf-8")

    assert "- **Status:** uncovered" in content
    assert "- **Requirements:** None" in content
    assert "- **Evidence:** None" in content
    assert "- **Evidence types:** None" in content
    assert "- **Confidence level:** None" in content
    assert "- **Missing evidence:** Yes" in content
    assert (
        "not currently linked to any software requirement"
        in content
    )
    assert (
        "- **Recommendation:** "
        "Compliance work should begin soon."
        in content
    )