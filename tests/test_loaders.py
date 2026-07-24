import json

import pytest

from compliance_assistant.loaders import (
    DataValidationError,
    load_evidence,
)


def test_load_evidence_with_valid_data(tmp_path):
    evidence_data = [
        {
            "id": "EVID-001",
            "title": "Encryption test result",
            "description": "Encryption test passed",
            "evidence_type": "Test Report",
            "source": "Pytest",
            "status": "Verified",
            "requirement_ids": ["REQ-001"],
            "confidence_level": "High",
        }
    ]

    evidence_file = tmp_path / "evidence.json"

    evidence_file.write_text(
        json.dumps(evidence_data),
        encoding="utf-8",
    )

    evidence_items = load_evidence(evidence_file)

    assert len(evidence_items) == 1

    evidence = evidence_items[0]

    assert evidence.id == "EVID-001"
    assert evidence.title == "Encryption test result"
    assert evidence.description == "Encryption test passed"
    assert evidence.evidence_type == "Test Report"
    assert evidence.source == "Pytest"
    assert evidence.status == "Verified"
    assert evidence.requirement_ids == ["REQ-001"]
    assert evidence.confidence_level == "High"


def test_load_evidence_rejects_missing_confidence_level(tmp_path):
    evidence_data = [
        {
            "id": "EVID-001",
            "title": "Encryption test result",
            "description": "Encryption test passed",
            "evidence_type": "Test Report",
            "source": "Pytest",
            "status": "Verified",
            "requirement_ids": ["REQ-001"],
        }
    ]

    evidence_file = tmp_path / "evidence.json"

    evidence_file.write_text(
        json.dumps(evidence_data),
        encoding="utf-8",
    )

    with pytest.raises(DataValidationError):
        load_evidence(evidence_file)