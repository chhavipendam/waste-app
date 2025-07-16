
import sqlite3

def view_all_users():
    conn = sqlite3.connect('waste.db')
    c = conn.cursor()
    c.execute("SELECT id, username FROM users")
    users = c.fetchall()
    conn.close()
    print("\n👥 All Registered Users:")
    for user in users:
        print(f"UserID: {user[0]}, Username: {user[1]}")

def waste_summary():
    conn = sqlite3.connect('waste.db')
    c = conn.cursor()
    c.execute("SELECT SUM(organic), SUM(plastic), SUM(e_waste), SUM(glass) FROM waste_logs")
    total = c.fetchone()
    conn.close()
    print("\n📊 Waste Summary (All Users)")
    print(f"Organic: {total[0] or 0} kg")
    print(f"Plastic: {total[1] or 0} kg")
    print(f"E-waste: {total[2] or 0} kg")
    print(f"Glass: {total[3] or 0} kg")
