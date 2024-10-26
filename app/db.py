import sqlite3


def init_db():
    conn = sqlite3.connect("app.db")
    c = conn.cursor()

    # Create requests table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            filename TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    # Create results table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id INTEGER,
            result REAL,
            FOREIGN KEY(request_id) REFERENCES requests(id)
        )
    """
    )

    conn.commit()
    conn.close()


def save_request(user, filename):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO requests (user, filename) VALUES (?, ?)
    """,
        (user, filename),
    )

    request_id = c.lastrowid  # Get the ID of the newly inserted request
    conn.commit()
    conn.close()

    return request_id


def save_result(request_id, result):
    conn = sqlite3.connect("app.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO results (request_id, result) VALUES (?, ?)
    """,
        (request_id, result),
    )

    conn.commit()
    conn.close()
