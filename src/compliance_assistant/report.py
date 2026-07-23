import json
from pathlib import Path


def save_json_report(report, path):
    """
    Save the compliance report as a JSON file.
    """
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )


def save_markdown_report(report, path):
    """
    Save the compliance report as a Markdown file.
    """
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Continuous Compliance Traceability Report",
        "",
    ]

    for item in report:

        if item["status"] == "covered":
            explanation = (
                "The obligation is linked to at least one software requirement "
                "and supporting engineering evidence has been recorded."
            )

        elif item["status"] == "partially covered":
            explanation = (
                "The obligation is linked to at least one software requirement, "
                "but no supporting engineering evidence has been recorded."
            )

        else:
            explanation = (
                "The obligation is not currently linked to any software "
                "requirement or supporting engineering evidence."
            )

        lines += [
            f"## {item['obligation_id']} — {item['obligation_title']}",
            f"- **Status:** {item['status']}",
            f"- **Risk level:** {item['risk_level']}",
            f"- **Priority:** {item['priority']}",
            f"- **Requirements:** {', '.join(item['requirement_ids']) or 'None'}",
            f"- **Evidence:** {', '.join(item['evidence_ids']) or 'None'}",
            f"- **Evidence types:** {', '.join(item['evidence_types']) or 'None'}",
            f"- **Confidence level:** {', '.join(item['confidence_levels']) or 'None'}",
            f"- **Missing evidence:** {'Yes' if item['missing_evidence'] else 'No'}",
            f"- **Explanation:** {explanation}",
            f"- **Recommendation:** {item['recommendation']}",
            "",
        ]

    output.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )
    