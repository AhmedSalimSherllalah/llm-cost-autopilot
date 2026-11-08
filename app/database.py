import sqlite3
from app.cost import calculate_savings

DB_NAME = "autopilot.db"


def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            complexity_score INTEGER NOT NULL,
            model TEXT NOT NULL,
            input_tokens INTEGER NOT NULL,
            output_tokens INTEGER NOT NULL,
            cost REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_request(
    prompt: str,
    complexity_score: int,
    model: str,
    input_tokens: int,
    output_tokens: int,
    cost: float
):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO requests (
            prompt,
            complexity_score,
            model,
            input_tokens,
            output_tokens,
            cost
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        prompt,
        complexity_score,
        model,
        input_tokens,
        output_tokens,
        cost
    ))

    connection.commit()
    connection.close()


def get_stats():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(cost),
            SUM(CASE WHEN model = 'gpt-6-luna' THEN 1 ELSE 0 END),
            SUM(CASE WHEN model = 'gpt-6.1-sol' THEN 1 ELSE 0 END)
        FROM requests
    """)

    stats = cursor.fetchone()
    connection.close()

    with sqlite3.connect(DB_NAME) as connection:
        rows = connection.execute("""
            SELECT model, input_tokens, output_tokens
            FROM requests
        """).fetchall()

    total_savings = sum(
        calculate_savings(model, input_tokens, output_tokens)
        for model, input_tokens, output_tokens in rows
)

    return {
        "total_requests": stats[0],
        "total_cost_usd": stats[1] or 0,
        "luna_requests": stats[2] or 0,
        "sol_requests": stats[3] or 0,
        "estimated_savings_usd": total_savings
    }