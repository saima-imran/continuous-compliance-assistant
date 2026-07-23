from dataclasses import dataclass
from typing import List

@dataclass
class Requirement:
    id: str
    title: str
    description: str
    source: str
    obligation_ids: List[str]

@dataclass
class ComplianceObligation:
    id: str
    title: str
    description: str
    source: str
    risk_level: str

@dataclass
class EvidenceItem:
    id: str
    title: str
    description: str
    source: str
    requirement_ids: List[str]
    status: str
    evidence_type: str
