
import sqlite3
from datetime import date

def register(username, password):
    conn = sqlite3.connect('waste.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registered successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Username already exists.")
    conn.close()

def login(username, password):
    conn = sqlite3.connect('waste.db')
    c = conn.cursor()
    c.execute("SELECT id, is_admin FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

def log_waste(user_id, organic, plastic, e_waste, glass):
    today = date.today().isoformat()
    conn = sqlite3.connect('waste.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO waste_logs (user_id, date, organic, plastic, e_waste, glass)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, today, organic, plastic, e_waste, glass))
    conn.commit()
    conn.close()
    print("🗑️ Waste logged for today!")
