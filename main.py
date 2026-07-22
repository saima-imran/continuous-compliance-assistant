import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from compliance_assistant.loaders import (
    DataValidationError,
    load_requirements,
    load_obligations,
    load_evidence,
)
from compliance_assistant.tracker import build_traceability_report
from compliance_assistant.report import save_json_report, save_markdown_report

def main():
    try:
        requirements = load_requirements("data/requirements.json")
        obligations = load_obligations("data/obligations.json")
        evidence = load_evidence("data/evidence.json")

        report = build_traceability_report(requirements, obligations, evidence)

        save_json_report(report, "output/compliance_report.json")
        save_markdown_report(report, "output/compliance_report.md")

        print("Success: reports created in the output folder.")
    except (FileNotFoundError, DataValidationError) as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()
