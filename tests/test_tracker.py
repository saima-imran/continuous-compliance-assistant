from types import SimpleNamespace

from compliance_assistant.tracker import build_traceability_report


def make_obligation(
    obligation_id="OBL-001",
    title="Protect personal data",
    risk_level="High",
):
    return SimpleNamespace(
        id=obligation_id,
        title=title,
        risk_level=risk_level,
    )


def make_requirement(
    requirement_id="REQ-001",
    obligation_ids=None,
):
    return SimpleNamespace(
        id=requirement_id,
        obligation_ids=obligation_ids or ["OBL-001"],
    )


def make_evidence(
    evidence_id="EVID-001",
    requirement_ids=None,
    evidence_type="Test Report",
    confidence_level="High",
):
    return SimpleNamespace(
        id=evidence_id,
        requirement_ids=requirement_ids or ["REQ-001"],
        evidence_type=evidence_type,
        confidence_level=confidence_level,
    )


def test_covered_obligation_has_low_priority():
    obligations = [
        make_obligation(risk_level="High"),
    ]

    requirements = [
        make_requirement(),
    ]

    evidence_items = [
        make_evidence(),
    ]

    report = build_traceability_report(
        requirements,
        obligations,
        evidence_items,
    )

    result = report[0]

    assert result["obligation_id"] == "OBL-001"
    assert result["status"] == "covered"
    assert result["priority"] == "Low"
    assert (
        result["recommendation"]
        == "Continue monitoring compliance."
    )
    assert result["requirement_ids"] == ["REQ-001"]
    assert result["evidence_ids"] == ["EVID-001"]
    assert result["evidence_types"] == ["Test Report"]
    assert result["confidence_levels"] == ["High"]
    assert result["missing_evidence"] is False


def test_partially_covered_high_risk_obligation():
    obligations = [
        make_obligation(risk_level="High"),
    ]

    requirements = [
        make_requirement(),
    ]

    evidence_items = []

    report = build_traceability_report(
        requirements,
        obligations,
        evidence_items,
    )

    result = report[0]

    assert result["status"] == "partially covered"
    assert result["risk_level"] == "High"
    assert result["priority"] == "High"
    assert (
        result["recommendation"]
        == "Immediate evidence collection required."
    )
    assert result["requirement_ids"] == ["REQ-001"]
    assert result["evidence_ids"] == []
    assert result["missing_evidence"] is True


def test_uncovered_medium_risk_obligation():
    obligations = [
        make_obligation(risk_level="Medium"),
    ]

    requirements = []
    evidence_items = []

    report = build_traceability_report(
        requirements,
        obligations,
        evidence_items,
    )

    result = report[0]

    assert result["status"] == "uncovered"
    assert result["risk_level"] == "Medium"
    assert result["priority"] == "Medium"
    assert (
        result["recommendation"]
        == "Compliance work should begin soon."
    )
    assert result["requirement_ids"] == []
    assert result["evidence_ids"] == []
    assert result["missing_evidence"] is True


def test_low_risk_uncovered_obligation():
    obligations = [
        make_obligation(risk_level="Low"),
    ]

    report = build_traceability_report(
        requirements=[],
        obligations=obligations,
        evidence_items=[],
    )

    result = report[0]

    assert result["status"] == "uncovered"
    assert result["priority"] == "Low"
    assert (
        result["recommendation"]
        == "Plan future compliance activities."
    )


def test_evidence_is_linked_to_correct_requirement():
    obligations = [
        make_obligation(),
    ]

    requirements = [
        make_requirement(
            requirement_id="REQ-001",
            obligation_ids=["OBL-001"],
        ),
        make_requirement(
            requirement_id="REQ-002",
            obligation_ids=["OBL-OTHER"],
        ),
    ]

    evidence_items = [
        make_evidence(
            evidence_id="EVID-001",
            requirement_ids=["REQ-001"],
        ),
        make_evidence(
            evidence_id="EVID-002",
            requirement_ids=["REQ-002"],
        ),
    ]

    report = build_traceability_report(
        requirements,
        obligations,
        evidence_items,
    )

    result = report[0]

    assert result["requirement_ids"] == ["REQ-001"]
    assert result["evidence_ids"] == ["EVID-001"]