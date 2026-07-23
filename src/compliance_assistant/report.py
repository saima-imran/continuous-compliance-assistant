import json
from pathlib import Path


def save_json_report(report, path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")


def save_markdown_report(report, path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = ["# Continuous Compliance Traceability Report", ""]

    for item in report:
        if item["missing_evidence"]:
            explanation = (
                "The obligation is linked to a requirement, but no supporting "
                "engineering evidence has been recorded."
            )
            recommended_action = (
                "Add evidence such as a test result, review record, design document, "
                "or runtime log."
            )
        else:
            explanation = (
                "The obligation is linked to both a requirement and supporting "
                "engineering evidence."
            )
            recommended_action = "No immediate evidence action is required."

        lines += [
            f"## {item['obligation_id']} — {item['obligation_title']}",
            f"- **Status:** {item['status']}",
            f"- **Risk level:** {item['risk_level']}",
            f"- **Requirements:** {', '.join(item['requirement_ids']) or 'None'}",
            f"- **Evidence:** {', '.join(item['evidence_ids']) or 'None'}",
            f"- **Evidence types:** {', '.join(item['evidence_types']) or 'None'}",
            f"- **Missing evidence:** {'Yes' if item['missing_evidence'] else 'No'}",
            f"- **Explanation:** {explanation}",
            f"- **Recommended action:** {recommended_action}",
            "",
        ]

    output.write_text("\n".join(lines), encoding="utf-8")