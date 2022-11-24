import sqlite3

class Admin:
    count = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password
        Admin.count += 1

    @staticmethod
    def total_admins():
        conn = sqlite3.connect('admin.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return len(rows)

    def __repr__(self):
        return f"{self.username} | {self.password}"

    def __len__(self):
        return Admin.count