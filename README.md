# Continuous Compliance Assistant

> A modular Python application that demonstrates compliance traceability, risk assessment, and explainable reporting using structured software engineering principles.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Testing](https://img.shields.io/badge/Testing-pytest-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Overview

Continuous Compliance Assistant is a Python-based software engineering project that demonstrates how regulatory obligations can be traced through software requirements and supporting engineering evidence.

The application loads structured compliance data, stores it in an SQLite database, analyses traceability relationships, evaluates compliance risk, generates explainable recommendations, and produces reports in Markdown and JSON.

The project demonstrates software engineering concepts including modular architecture, relational database design, automated testing, and continuous integration.

---

# Features

- Load compliance data from JSON files
- Store compliance information in SQLite
- Manage obligations, requirements, and evidence
- Support many-to-many traceability relationships
- Assess compliance coverage and risk
- Generate explainable recommendations
- Produce Markdown and JSON reports
- Automated testing using pytest
- Continuous Integration with GitHub Actions

---

# System Architecture

```text
                 JSON DATA

        obligations.json
        requirements.json
        evidence.json
               │
               ▼
          loaders.py
               │
               ▼
         database.py
               │
               ▼
          tracker.py
               │
               ▼
           report.py
          │          │
          ▼          ▼

 compliance_report.md
 compliance_report.json
```

---

# Application Workflow

```text
Start Application
        │
        ▼
Load JSON Data
        │
        ▼
Validate Input
        │
        ▼
Store in SQLite
        │
        ▼
Perform Traceability
        │
        ▼
Assess Compliance Risk
        │
        ▼
Generate Recommendations
        │
        ▼
Produce Reports
```

---

# Project Structure

```text
continuous-compliance-assistant/

├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│   ├── obligations.json
│   ├── requirements.json
│   └── evidence.json
│
├── output/
│   ├── compliance_report.md
│   └── compliance_report.json
│
├── src/
│   └── compliance_assistant/
│       ├── __init__.py
│       ├── database.py
│       ├── loaders.py
│       ├── models.py
│       ├── tracker.py
│       └── report.py
│
├── tests/
│   ├── test_database.py
│   ├── test_loaders.py
│   ├── test_report.py
│   └── test_tracker.py
│
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Module Responsibilities

| Module | Responsibility |
|---------|----------------|
| `main.py` | Coordinates the application workflow |
| `loaders.py` | Loads compliance data from JSON files |
| `models.py` | Defines the project's data models |
| `database.py` | Manages SQLite database operations |
| `tracker.py` | Performs compliance analysis and traceability |
| `report.py` | Generates Markdown and JSON reports |

---

# Database Design

The SQLite database contains five tables.

| Table | Purpose |
|--------|---------|
| obligations | Stores regulatory obligations |
| requirements | Stores software requirements |
| evidence | Stores supporting engineering evidence |
| requirement_obligations | Links requirements to obligations |
| evidence_requirements | Links evidence to requirements |

Relationship model:

```text
Obligations
      ▲
      │
Requirement_Obligations
      │
      ▼
Requirements
      ▲
      │
Evidence_Requirements
      │
      ▼
Evidence
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/continuous-compliance-assistant.git
```

Navigate into the project.

```bash
cd continuous-compliance-assistant
```

Create a virtual environment (optional).

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the application.

```bash
python main.py
```

Generated reports are written to:

```text
output/compliance_report.md
```

and

```text
output/compliance_report.json
```

---

# Running the Tests

Run the complete test suite.

```bash
pytest
```

Run only the database tests.

```bash
pytest tests/test_database.py -v
```

GitHub Actions automatically executes the test suite whenever code is pushed to the repository.

---

# Example Output

```text
Obligation:
Protect personal data

Requirement:
Encrypt stored personal data

Evidence:
Encryption test report

Compliance Status:
Covered

Risk:
Low

Recommendation:
Continue monitoring compliance.
```

---

# Technologies Used

- Python
- SQLite
- JSON
- pytest
- Git
- GitHub Actions
- Markdown

---

# Software Engineering Principles

This project demonstrates:

- Modular architecture
- Separation of concerns
- Relational database design
- Many-to-many relationships
- Data validation
- Compliance traceability
- Risk assessment
- Explainable recommendation generation
- Automated testing
- Continuous integration
- Structured report generation

---

# Future Improvements

Possible future enhancements include:

- Command-line interface
- REST API
- Web dashboard
- Authentication and user management
- Support for additional compliance frameworks
- AI-assisted compliance recommendations
- Audit logging and version history

---

# Author

**Saima Imran**

Software Engineering Portfolio Project

This project demonstrates practical software engineering techniques for modelling continuous compliance, software traceability, relational database design, automated testing, and explainable reporting.
