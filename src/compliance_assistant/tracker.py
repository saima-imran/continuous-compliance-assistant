def build_traceability_report(requirements, obligations, evidence_items):
    evidence_by_requirement = {}

    for evidence in evidence_items:
        for requirement_id in evidence.requirement_ids:
            evidence_by_requirement.setdefault(requirement_id, []).append(evidence)

    report = []

    for obligation in obligations:
        linked_requirements = [
            requirement
            for requirement in requirements
            if obligation.id in requirement.obligation_ids
        ]

        linked_evidence = []

        for requirement in linked_requirements:
            linked_evidence.extend(
                evidence_by_requirement.get(requirement.id, [])
            )

        if linked_requirements and linked_evidence:
            status = "covered"
        elif linked_requirements:
            status = "partially covered"
        else:
            status = "uncovered"

        report.append(
            {
                "obligation_id": obligation.id,
                "obligation_title": obligation.title,
                "status": status,
                "risk_level": obligation.risk_level,
                "requirement_ids": [
                    requirement.id for requirement in linked_requirements
                ],
                "evidence_ids": [
                    evidence.id for evidence in linked_evidence
                ],
                "evidence_types": [
                    evidence.evidence_type for evidence in linked_evidence
                ],
                "missing_evidence": status != "covered",
            }
        )

    return report
