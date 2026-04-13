import sqlite3
from datetime import date
from werkzeug.security import generate_password_hash

DATABASE = "spendly.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()


def register_user(name, email, password):
    """Create a new user with hashed password. Returns user_id on success, None on failure."""
    conn = get_db()
    try:
        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (name, email, generate_password_hash(password))
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        conn.close()
        return None


def seed_db():
    conn = get_db()
    cursor = conn.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    cursor = conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123"))
    )
    user_id = cursor.lastrowid

    today = date.today()
    year = today.year
    month = today.month

    expenses = [
        (user_id, 12.50, "Food", f"{year}-{month:02d}-03", "Lunch at cafe"),
        (user_id, 45.00, "Transport", f"{year}-{month:02d}-05", "Uber ride"),
        (user_id, 120.00, "Bills", f"{year}-{month:02d}-07", "Electricity bill"),
        (user_id, 30.00, "Health", f"{year}-{month:02d}-10", "Pharmacy"),
        (user_id, 25.99, "Entertainment", f"{year}-{month:02d}-12", "Movie streaming"),
        (user_id, 89.99, "Shopping", f"{year}-{month:02d}-15", "New shoes"),
        (user_id, 15.00, "Food", f"{year}-{month:02d}-20", "Groceries"),
        (user_id, 8.50, "Other", f"{year}-{month:02d}-22", "Parking fee"),
    ]

    conn.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        expenses
    )
    conn.commit()
    conn.close()
