from pathlib import Path
import sqlite3

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Task Manager API",
    description="A FastAPI CRUD application connected to SQLite",
    version="3.0.0"
)


# Absolute path of the week-3 folder
BASE_DIR = Path(__file__).resolve().parent

# Database will be created inside week-3
DATABASE_PATH = BASE_DIR / "tasks.db"


def get_database_connection():
    """
    Open a connection to the SQLite database.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    # Allows rows to be accessed using column names:
    # row["id"], row["title"], row["done"]
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create the tasks table and insert three starter tasks
    only when the table is empty.
    """

    with get_database_connection() as connection:

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
            """
        )

        result = connection.execute(
            "SELECT COUNT(*) AS task_count FROM tasks"
        ).fetchone()

        task_count = result["task_count"]

        if task_count == 0:
            example_tasks = [
                ("Learn SQLite", 0),
                ("Connect FastAPI to a database", 0),
                ("Complete Week 3 Assignment", 0)
            ]

            connection.executemany(
                """
                INSERT INTO tasks (title, done)
                VALUES (?, ?)
                """,
                example_tasks
            )

        connection.commit()


def row_to_task(row):
    """
    Convert a SQLite row into a JSON-compatible dictionary.
    """

    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])
    }


# Create database and table when the application starts
initialize_database()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Week 3 Task Manager API",
        "database": "SQLite"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }


@app.get("/tasks")
def get_tasks():
    """
    Read all tasks from the SQLite database.
    """

    with get_database_connection() as connection:

        rows = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            ORDER BY id
            """
        ).fetchall()

        return [row_to_task(row) for row in rows]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """
    Read one task from the SQLite database using its ID.
    """

    with get_database_connection() as connection:

        row = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            WHERE id = ?
            """,
            (task_id,)
        ).fetchone()

        if row is None:
            return JSONResponse(
                status_code=404,
                content={"error": "Task not found"}
            )

        return row_to_task(row)