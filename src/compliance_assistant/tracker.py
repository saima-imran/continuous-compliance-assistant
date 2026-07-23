def build_traceability_report(requirements, obligations, evidence_items):
    evidence_by_requirement = {}

    for evidence in evidence_items:
        for requirement_id in evidence.requirement_ids:
            evidence_by_requirement.setdefault(
                requirement_id,
                [],
            ).append(evidence)

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
                evidence_by_requirement.get(
                    requirement.id,
                    [],
                )
            )

        if linked_requirements and linked_evidence:
            status = "covered"
        elif linked_requirements:
            status = "partially covered"
        else:
            status = "uncovered"

        if status == "covered":
            recommendation = "Continue monitoring compliance."
            priority = "Low"

        elif status == "partially covered":
            if obligation.risk_level == "High":
                recommendation = (
                    "Immediate evidence collection required."
                )
                priority = "High"

            elif obligation.risk_level == "Medium":
                recommendation = "Add supporting evidence soon."
                priority = "Medium"

            else:
                recommendation = "Schedule evidence collection."
                priority = "Low"

        else:
            if obligation.risk_level == "High":
                recommendation = (
                    "Critical compliance gap. "
                    "Immediate action required."
                )
                priority = "High"

            elif obligation.risk_level == "Medium":
                recommendation = (
                    "Compliance work should begin soon."
                )
                priority = "Medium"

            else:
                recommendation = (
                    "Plan future compliance activities."
                )
                priority = "Low"

        report.append(
            {
                "obligation_id": obligation.id,
                "obligation_title": obligation.title,
                "status": status,
                "risk_level": obligation.risk_level,
                "priority": priority,
                "recommendation": recommendation,
                "requirement_ids": [
                    requirement.id
                    for requirement in linked_requirements
                ],
                "evidence_ids": [
                    evidence.id
                    for evidence in linked_evidence
                ],
                "evidence_types": [
                    evidence.evidence_type
                    for evidence in linked_evidence
                ],
                "confidence_levels": [
                    evidence.confidence_level
                    for evidence in linked_evidence
                ],
                "missing_evidence": status != "covered",
            }
        )

    return report