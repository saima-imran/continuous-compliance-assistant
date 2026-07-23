# Continuous Compliance Assistant

> A modular Python application that demonstrates compliance traceability, risk assessment, and explainable reporting using structured software engineering principles.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-success)
![Architecture](https://img.shields.io/badge/Architecture-Modular-orange)

---

## Table of Contents

- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Application Workflow](#application-workflow)
- [Project Structure](#project-structure)
- [Module Responsibilities](#module-responsibilities)
- [Data Model](#data-model)
- [Risk Assessment](#risk-assessment)
- [Recommendation Engine](#recommendation-engine)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Example Output](#example-output)
- [Design Decisions](#design-decisions)
- [Software Engineering Principles](#software-engineering-principles)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

# Overview

The **Continuous Compliance Assistant** is a Python-based software engineering project that demonstrates how regulatory obligations can be traced through software requirements and supporting engineering evidence.

The application analyses compliance coverage, evaluates regulatory risk, generates explainable recommendations, and produces structured reports in both Markdown and JSON.

This project was developed as a software engineering portfolio demonstrating clean architecture, modular programming, data validation, traceability, and automated reporting.

---

# Project Objectives

The project aims to demonstrate:

- Compliance traceability
- Modular software architecture
- Structured JSON processing
- Data validation
- Risk assessment
- Explainable recommendation generation
- Automated report generation

---

# Features

- Regulatory obligation management
- Requirement traceability
- Evidence management
- Compliance coverage analysis
- Risk assessment (High / Medium / Low)
- Explainable recommendation engine
- Evidence confidence tracking
- Markdown report generation
- JSON report generation
- Modular Python architecture

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
        models.py
               │
               ▼
        tracker.py
               │
               ▼
        report.py
          │         │
          ▼         ▼

 compliance_report.md
 compliance_report.json
```

---

# Application Workflow

```text
Start Application

        │
        ▼

Load JSON Files

        │
        ▼

Validate Input Data

        │
        ▼

Create Data Models

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
│       ├── loaders.py
│       ├── models.py
│       ├── tracker.py
│       └── report.py
│
├── tests/
│   └── test_placeholder.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Module Responsibilities

| Module | Responsibility |
|---------|----------------|
| `main.py` | Coordinates the complete application workflow |
| `loaders.py` | Loads and validates JSON datasets |
| `models.py` | Defines the project data models |
| `tracker.py` | Performs traceability, compliance analysis, risk assessment, and recommendation generation |
| `report.py` | Generates Markdown and JSON reports |

---

# Data Model

The application uses three primary entities.

## Obligation

Represents a regulatory obligation that must be satisfied.

## Requirement

Represents one or more software requirements linked to obligations.

## Evidence

Represents engineering artefacts that demonstrate implementation or verification.

Each evidence record also stores a confidence level describing the reliability of the supporting evidence.

---

# Risk Assessment

Each obligation includes a predefined priority level.

The application combines:

- compliance status
- available evidence
- obligation priority

to determine the overall compliance risk.

Supported priorities:

- High
- Medium
- Low

---

# Recommendation Engine

Recommendations are generated using transparent rule-based logic.

| Compliance Status | Recommendation |
|-------------------|---------------|
| Covered | Continue monitoring compliance. |
| Partially Covered | Collect additional supporting evidence. |
| Uncovered | Begin compliance activities immediately. |

The recommendation engine is intentionally explainable, allowing every decision to be traced back to the available project data.

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

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Application

Execute the application.

```bash
python main.py
```

Generated reports will be written to:

```text
output/compliance_report.md
```

and

```text
output/compliance_report.json
```

---

# Example Output

```text
Obligation: OBL-001

Status:
Covered

Priority:
High

Evidence Confidence:
High

Recommendation:
Continue monitoring compliance.
```

---

# Design Decisions

## Why JSON?

JSON separates application logic from project data and makes datasets easy to extend.

## Why Dataclasses?

Python dataclasses provide concise, readable, and maintainable representations of domain entities.

## Why Modular Design?

Separating responsibilities across modules improves maintainability, readability, and future extensibility.

## Why Rule-Based Recommendations?

Transparent rule-based reasoning provides predictable and explainable compliance decisions.

---

# Software Engineering Principles

This project demonstrates:

- Modular programming
- Separation of concerns
- Data validation
- Explainable decision making
- Automated report generation
- Traceability
- Version control with Git
- Object-oriented design using dataclasses

---

# Future Improvements

Potential future enhancements include:

- Comprehensive unit testing using pytest
- Database integration
- REST API
- Interactive web dashboard
- Data visualization
- AI-assisted recommendation generation
- Compliance knowledge graph integration

---

# Author

**Saima Imran**

Software Engineering Portfolio Project

This project demonstrates practical software engineering techniques applied to a simplified Continuous Compliance workflow, including traceability, risk assessment, explainable reporting, and modular Python development.