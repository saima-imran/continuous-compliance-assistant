from types import SimpleNamespace

from compliance_assistant.database import (
    create_connection,
    create_tables,
    get_evidence,
    get_obligations,
    get_requirements,
    insert_evidence,
    insert_obligation,
    insert_requirement,
    link_evidence_to_requirement,
    link_requirement_to_obligation,
)


def test_create_tables(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
    )

    table_names = {row[0] for row in cursor.fetchall()}

    expected_tables = {
        "obligations",
        "requirements",
        "evidence",
        "requirement_obligations",
        "evidence_requirements",
    }

    assert expected_tables.issubset(table_names)

    connection.close()


def test_insert_obligation(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    obligation = SimpleNamespace(
        id="OBL-001",
        title="Protect personal data",
        description="Personal data must be protected.",
        risk_level="high",
    )

    insert_obligation(connection, obligation)

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id, title, description, risk_level
        FROM obligations
        WHERE id = ?
        """,
        ("OBL-001",),
    )

    row = cursor.fetchone()

    assert row == (
        "OBL-001",
        "Protect personal data",
        "Personal data must be protected.",
        "high",
    )

    connection.close()


def test_insert_requirement(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    requirement = SimpleNamespace(
        id="REQ-001",
        title="Encrypt stored data",
        description="Stored personal data must be encrypted.",
        priority="high",
    )

    insert_requirement(connection, requirement)

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id, title, description, priority
        FROM requirements
        WHERE id = ?
        """,
        ("REQ-001",),
    )

    row = cursor.fetchone()

    assert row == (
        "REQ-001",
        "Encrypt stored data",
        "Stored personal data must be encrypted.",
        "high",
    )

    connection.close()


def test_insert_evidence(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    evidence = SimpleNamespace(
        id="EVD-001",
        title="Encryption test report",
        description="A test report confirms encryption is enabled.",
        evidence_type="test_report",
        source="security-tests",
        status="valid",
        confidence_level="high",
    )

    insert_evidence(connection, evidence)

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT
            id,
            title,
            description,
            evidence_type,
            source,
            status,
            confidence_level
        FROM evidence
        WHERE id = ?
        """,
        ("EVD-001",),
    )

    row = cursor.fetchone()

    assert row == (
        "EVD-001",
        "Encryption test report",
        "A test report confirms encryption is enabled.",
        "test_report",
        "security-tests",
        "valid",
        "high",
    )

    connection.close()


def test_get_obligations(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    obligation = SimpleNamespace(
        id="OBL-001",
        title="Protect personal data",
        description="Personal data must be protected.",
        risk_level="high",
    )

    insert_obligation(connection, obligation)

    results = get_obligations(connection)

    assert len(results) == 1
    assert results[0] == (
        "OBL-001",
        "Protect personal data",
        "Personal data must be protected.",
        "high",
    )

    connection.close()


def test_get_requirements(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    requirement = SimpleNamespace(
        id="REQ-001",
        title="Encrypt stored data",
        description="Stored personal data must be encrypted.",
        priority="high",
    )

    insert_requirement(connection, requirement)

    results = get_requirements(connection)

    assert len(results) == 1
    assert results[0] == (
        "REQ-001",
        "Encrypt stored data",
        "Stored personal data must be encrypted.",
        "high",
    )

    connection.close()


def test_get_evidence(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    evidence = SimpleNamespace(
        id="EVD-001",
        title="Encryption test report",
        description="A test report confirms encryption is enabled.",
        evidence_type="test_report",
        source="security-tests",
        status="valid",
        confidence_level="high",
    )

    insert_evidence(connection, evidence)

    results = get_evidence(connection)

    assert len(results) == 1
    assert results[0] == (
        "EVD-001",
        "Encryption test report",
        "A test report confirms encryption is enabled.",
        "test_report",
        "security-tests",
        "valid",
        "high",
    )

    connection.close()


def test_link_requirement_to_obligation(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    obligation = SimpleNamespace(
        id="OBL-001",
        title="Protect personal data",
        description="Personal data must be protected.",
        risk_level="high",
    )

    requirement = SimpleNamespace(
        id="REQ-001",
        title="Encrypt stored data",
        description="Stored personal data must be encrypted.",
        priority="high",
    )

    insert_obligation(connection, obligation)
    insert_requirement(connection, requirement)

    link_requirement_to_obligation(
        connection,
        requirement_id="REQ-001",
        obligation_id="OBL-001",
    )

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT requirement_id, obligation_id
        FROM requirement_obligations
        """
    )

    row = cursor.fetchone()

    assert row == ("REQ-001", "OBL-001")

    connection.close()


def test_link_evidence_to_requirement(tmp_path):
    database_path = tmp_path / "test.db"

    connection = create_connection(database_path)
    create_tables(connection)

    requirement = SimpleNamespace(
        id="REQ-001",
        title="Encrypt stored data",
        description="Stored personal data must be encrypted.",
        priority="high",
    )

    evidence = SimpleNamespace(
        id="EVD-001",
        title="Encryption test report",
        description="A test report confirms encryption is enabled.",
        evidence_type="test_report",
        source="security-tests",
        status="valid",
        confidence_level="high",
    )

    insert_requirement(connection, requirement)
    insert_evidence(connection, evidence)

    link_evidence_to_requirement(
        connection,
        evidence_id="EVD-001",
        requirement_id="REQ-001",
    )

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT evidence_id, requirement_id
        FROM evidence_requirements
        """
    )

    row = cursor.fetchone()

    assert row == ("EVD-001", "REQ-001")

    connection.close()