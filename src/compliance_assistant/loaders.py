import json
from pathlib import Path

from .models import Requirement, ComplianceObligation, EvidenceItem


class DataValidationError(Exception):
    pass


def _read_json(path):
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        data = json.loads(
            file_path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise DataValidationError(
            f"Invalid JSON in {file_path}: {exc}"
        ) from exc

    if not isinstance(data, list):
        raise DataValidationError(
            f"{file_path} must contain a JSON list."
        )

    return data


def _validate(records, required_fields, label):
    seen = set()

    for index, record in enumerate(records, start=1):
        missing = required_fields - record.keys()

        if missing:
            raise DataValidationError(
                f"{label} record {index} is missing: {sorted(missing)}"
            )

        if record["id"] in seen:
            raise DataValidationError(
                f"Duplicate {label} ID: {record['id']}"
            )

        seen.add(record["id"])


def load_requirements(path):
    records = _read_json(path)

    _validate(
        records,
        {
            "id",
            "title",
            "description",
            "source",
            "obligation_ids",
        },
        "requirement",
    )

    return [Requirement(**record) for record in records]


def load_obligations(path):
    records = _read_json(path)

    _validate(
        records,
        {
            "id",
            "title",
            "description",
            "source",
            "risk_level",
        },
        "obligation",
    )

    return [
        ComplianceObligation(**record)
        for record in records
    ]


def load_evidence(path):
    records = _read_json(path)

    _validate(
        records,
        {
            "id",
            "title",
            "description",
            "source",
            "requirement_ids",
            "status",
            "evidence_type",
            "confidence_level",
        },
        "evidence",
    )

    return [EvidenceItem(**record) for record in records]