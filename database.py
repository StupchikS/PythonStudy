import sqlite3 as sq


with sq.connect("profile.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    summa REAL,
    data TEXT
    )
    """)


