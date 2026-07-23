 Continuous Compliance Assistant

A Python-Based Software Engineering Project for ComplianceTraceability, Risk Assessment, and Explainable Reporting



📚 Table of Contents

Introduction

Project Motivation

Continuous ComplianceBackground

Project Objectives

Key Features

System Architecture

Application Workflow

Project Structure

Module Responsibilities

Data Model

Recommendation Engine

Installation

Running the Application

Example Output

Design Decisions

Software Engineering Principles

Current Limitations

Future Work

Lessons Learned

Author

📖 Introduction

Continuous Compliance Assistant is a modular Python application thatdemonstrates how software engineering practices can be applied toregulatory compliance.

The project models three important artefacts:

Compliance obligations

Software requirements

Engineering evidence

It analyses the relationships between them to determine compliancestatus, assess regulatory risk, generate recommendations, and produceexplainable reports in Markdown and JSON.

The project is intended as a software engineering portfoliodemonstrating clean architecture, traceability, structured dataprocessing, and explainable rule-based decision making.

🎯 Project Motivation

Software systems in regulated domains must demonstrate compliancethroughout the development lifecycle rather than only at release time.

This project explores a simplified Continuous Compliance workflow byconnecting regulatory obligations with software requirements andengineering evidence.

Instead of replacing engineers, the application supports them byproducing consistent, transparent compliance assessments.

🌍 Continuous Compliance Background

Continuous Compliance integrates compliance activities into everydaysoftware development.

This project demonstrates a simplified workflow:

Define compliance obligations.

Link obligations to software requirements.

Record engineering evidence.

Evaluate coverage.

Assess risk.

Produce explainable reports.

🎯 Project Objectives

Demonstrate traceability.

Validate structured datasets.

Assess compliance coverage.

Evaluate regulatory risk.

Generate recommendations.

Produce Markdown and JSON reports.

Showcase software engineering best practices.

✨ Key Features

Feature                       Description

Compliance Traceability       Links obligations, requirements, andevidence.

Risk Assessment               Supports High, Medium, and Low riskobligations.

Recommendation Engine         Generates explainable recommendations.

Evidence Confidence           Records confidence levels for engineeringevidence.

Markdown Reporting            Human-readable compliance reports.

JSON Reporting                Machine-readable output for integration.

Modular Architecture          Separation of concerns across modules.

🏗️ System Architecture

flowchart TD

A[obligations.json]
B[requirements.json]
C[evidence.json]

A --> D(loaders.py)
B --> D
C --> D

D --> E(models.py)
E --> F(tracker.py)
F --> G(report.py)

G --> H[compliance_report.md]
G --> I[compliance_report.json]

🔄 Application Workflow

flowchart TD
A[python main.py] --> B[Load JSON files]
B --> C[Validate data]
C --> D[Create Python objects]
D --> E[Trace obligations]
E --> F[Evaluate compliance]
F --> G[Assess risk]
G --> H[Generate recommendations]
H --> I[Create Markdown and JSON reports]

📁 Project Structure

ContinuousComplianceAssistant/
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
│       ├── models.py
│       ├── loaders.py
│       ├── tracker.py
│       ├── report.py
│       └── __init__.py
│
├── tests/
│   └── test_placeholder.py
│
├── main.py
├── requirements.txt
└── README.md

📦 Module Responsibilities

Module                  Responsibility

main.py               Coordinates the application workflow.

models.py             Defines Obligation, Requirement, and Evidencedata models.

loaders.py            Loads and validates JSON datasets.

tracker.py            Performs traceability, compliance analysis,risk assessment, and recommendation generation.

report.py             Produces Markdown and JSON reports.

🧩 Data Model

Entity                            Purpose

Obligation                        Represents a regulatory obligation.

Requirement                       Represents a software requirementlinked to obligations.

💡 Recommendation Engine

Recommendations are generated using transparent rule-based logic.

Status              Typical Recommendation

Covered             Continue monitoring compliance.Partially Covered   Add supporting evidence soon.Uncovered           Begin compliance activities or collect evidence.

The recommendation process is intentionally explainable so every outputcan be traced back to its inputs.

⚙️ Installation

git clone <repository-url>
cd ContinuousComplianceAssistant
pip install -r requirements.txt

▶️ Running the Application

python main.py

Generated reports:

output/compliance_report.md

output/compliance_report.json

📄 Example Output

OBL-001
Status: Covered
Risk Level: High
Priority: Low
Confidence Level: High

Recommendation:
Continue monitoring compliance.

🧠 Design Decisions

Why JSON?

JSON keeps application data separate from business logic, makingdatasets easy to maintain.

Why Dataclasses?

Dataclasses provide clear, concise representations of domain entitieswhile reducing boilerplate code.

Why Modular Architecture?

Each module has a single responsibility, improving maintainability,readability, and extensibility.

Why Rule-Based Reasoning?

Transparent rules make recommendations easy to understand, verify, andexplain.

🏛️ Software Engineering Principles

Separation of Concerns

Modular Design

Data Validation

Traceability

Explainable Decision Making

Automated Report Generation

Version Control with Git

⚠️ Current Limitations

Static JSON datasets

Rule-based recommendations

No database

No web interface

Placeholder test suite

🚀 Future Work

Unit tests with pytest

Database integration

REST API

Dashboard visualisation

AI-assisted recommendation engine

Knowledge graph integration

📚 Lessons Learned

This project strengthened practical understanding of:

Modular Python application design

Traceability in software engineering

Data validation

Rule-based reasoning

Automated reporting

Git and incremental development

👤 Author

Developed as a software engineering portfolio project demonstratingContinuous Compliance concepts using Python.
