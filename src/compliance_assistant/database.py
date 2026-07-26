import sqlite3
from pathlib import Path


def create_connection(database_path):
    """
    Create and return a connection to the SQLite database.
    """
    path = Path(database_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    return sqlite3.connect(path)


def create_tables(connection):
    """
    Create the database tables used by the application.
    """
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS obligations (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            risk_level TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS requirements (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS evidence (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            evidence_type TEXT NOT NULL,
            source TEXT NOT NULL,
            status TEXT NOT NULL,
            confidence_level TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS requirement_obligations (
            requirement_id TEXT NOT NULL,
            obligation_id TEXT NOT NULL,
            PRIMARY KEY (requirement_id, obligation_id),
            FOREIGN KEY (requirement_id)
                REFERENCES requirements(id),
            FOREIGN KEY (obligation_id)
                REFERENCES obligations(id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS evidence_requirements (
            evidence_id TEXT NOT NULL,
            requirement_id TEXT NOT NULL,
            PRIMARY KEY (evidence_id, requirement_id),
            FOREIGN KEY (evidence_id)
                REFERENCES evidence(id),
            FOREIGN KEY (requirement_id)
                REFERENCES requirements(id)
        )
        """
    )

    connection.commit()


def insert_obligation(connection, obligation):
    """
    Insert one compliance obligation into the database.
    """
    query = """
    INSERT INTO obligations (
        id,
        title,
        description,
        risk_level
    )
    VALUES (?, ?, ?, ?)
    """

    connection.execute(
        query,
        (
            obligation.id,
            obligation.title,
            obligation.description,
            obligation.risk_level,
        ),
    )

    connection.commit()


def insert_requirement(connection, requirement):
    """
    Insert one software requirement into the database.
    """
    query = """
    INSERT INTO requirements (
        id,
        title,
        description,
        priority
    )
    VALUES (?, ?, ?, ?)
    """

    connection.execute(
        query,
        (
            requirement.id,
            requirement.title,
            requirement.description,
            requirement.priority,
        ),
    )

    connection.commit()


def insert_evidence(connection, evidence):
    """
    Insert one evidence item into the database.
    """
    query = """
    INSERT INTO evidence (
        id,
        title,
        description,
        evidence_type,
        source,
        status,
        confidence_level
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    connection.execute(
        query,
        (
            evidence.id,
            evidence.title,
            evidence.description,
            evidence.evidence_type,
            evidence.source,
            evidence.status,
            evidence.confidence_level,
        ),
    )

    connection.commit()

def get_obligations(connection):
    """
    Return all obligations stored in the database.
    """
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, description, risk_level
        FROM obligations
        ORDER BY id
        """
    )

    return cursor.fetchall()


def get_requirements(connection):
    """
    Return all requirements stored in the database.
    """
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, description, priority
        FROM requirements
        ORDER BY id
        """
    )

    return cursor.fetchall()


def get_evidence(connection):
    """
    Return all evidence stored in the database.
    """
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
        ORDER BY id
        """
    )

    return cursor.fetchall()
def link_requirement_to_obligation(
    connection,
    requirement_id,
    obligation_id,
):
    """
    Link one requirement to one obligation.
    """
    connection.execute(
        """
        INSERT INTO requirement_obligations (
            requirement_id,
            obligation_id
        )
        VALUES (?, ?)
        """,
        (
            requirement_id,
            obligation_id,
        ),
    )

    connection.commit()


def link_evidence_to_requirement(
    connection,
    evidence_id,
    requirement_id,
):
    """
    Link one evidence item to one requirement.
    """
    connection.execute(
        """
        INSERT INTO evidence_requirements (
            evidence_id,
            requirement_id
        )
        VALUES (?, ?)
        """,
        (
            evidence_id,
            requirement_id,
        ),
    )

    connection.commit()