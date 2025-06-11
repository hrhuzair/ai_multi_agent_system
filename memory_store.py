import sqlite3

def init_memory():
    conn = sqlite3.connect("memory.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        format TEXT,
        intent TEXT,
        fields TEXT,
        action TEXT
    )
    """)
    conn.commit()
    return conn

def log_trace(format, intent, fields, action):
    conn = init_memory()
    conn.execute(
        "INSERT INTO logs (timestamp, format, intent, fields, action) VALUES (datetime('now'), ?, ?, ?, ?)",
        (format, intent, str(fields), action)
    )
    conn.commit()
    conn.close()
