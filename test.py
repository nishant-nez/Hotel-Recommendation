import sqlite3

# admin credentials database
conn = sqlite3.connect('admin.db')
cur = conn.cursor()

create_table = '''CREATE TABLE IF NOT EXISTS admin (id INT PRIMARY KEY, username TEXT, password TEXT)'''
cur.execute(create_table)

insert_first = '''INSERT INTO admin VALUES (1, 'firstuser', 'admin450')'''
cur.execute(insert_first)

conn.commit()
conn.close()