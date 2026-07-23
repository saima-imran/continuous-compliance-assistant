import json
from pathlib import Path


def save_json_report(report, path):
    """
    Save the compliance report as a JSON file.

    JSON is useful because it is machine-readable. Other programs,
    dashboards, APIs, or AI systems can process this report later.
    """
    output = Path(path)

    # Create the output folder if it does not already exist.
    output.parent.mkdir(parents=True, exist_ok=True)

    # Convert the Python report into formatted JSON and save it.
    output.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )


def save_markdown_report(report, path):
    """
    Save the compliance report as a Markdown file.

    Markdown is useful because it is human-readable and displays
    clearly on GitHub and in many documentation tools.
    """
    output = Path(path)

    # Create the output folder if it does not already exist.
    output.parent.mkdir(parents=True, exist_ok=True)

    # Start the report with a main heading.
    lines = [
        "# Continuous Compliance Traceability Report",
        "",
    ]

    # Process every obligation contained in the report.
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
                "The obligation is not currently linked to any software requirement "
                "or supporting engineering evidence."
            )

        # Add the current obligation and its analysis to the report.
        lines += [
            f"## {item['obligation_id']} — {item['obligation_title']}",
            f"- **Status:** {item['status']}",
            f"- **Risk level:** {item['risk_level']}",
            f"- **Priority:** {item['priority']}",
            (
                f"- **Requirements:** "
                f"{', '.join(item['requirement_ids']) or 'None'}"
            ),
            (
                f"- **Evidence:** "
                f"{', '.join(item['evidence_ids']) or 'None'}"
            ),
            (
                f"- **Evidence types:** "
                f"{', '.join(item['evidence_types']) or 'None'}"
            ),
            (
                f"- **Missing evidence:** "
                f"{'Yes' if item['missing_evidence'] else 'No'}"
            ),
            f"- **Explanation:** {explanation}",
            f"- **Recommendation:** {item['recommendation']}",
            "",
        ]

    # Join all report lines and save them as a Markdown file.
    output.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )