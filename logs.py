import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            ip TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS blacklist (
            ip TEXT PRIMARY KEY
        )
    """)
    conn.commit()
    conn.close()

def log_event(username, ip, status):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO logs (username, ip, status, timestamp) VALUES (?, ?, ?, ?)",
        (username, ip, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

def is_blacklisted(ip):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT ip FROM blacklist WHERE ip=?", (ip,))
    result = c.fetchone()
    conn.close()
    return result is not None

def blacklist_ip(ip):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO blacklist VALUES (?)", (ip,))
    conn.commit()
    conn.close()
