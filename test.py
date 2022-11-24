import sqlite3

# admin credentials database
conn = sqlite3.connect('admin.db')
cur = conn.cursor()

# create_table = '''CREATE TABLE IF NOT EXISTS admin (id INT PRIMARY KEY, username TEXT, password TEXT)'''
# cur.execute(create_table)

# insert_first = '''INSERT INTO admin VALUES (1, 'firstuser', 'admin450')'''
# cur.execute(insert_first)
# insert_first = '''INSERT INTO admin VALUES (2, 'seconduser', 'admin451')'''
# cur.execute(insert_first)
# insert_first = '''INSERT INTO admin VALUES (3, 'thirduser', 'admin452')'''
# cur.execute(insert_first)
insert_main = '''INSERT INTO admin VALUES (4, 'admin', 'admin123')'''
cur.execute(insert_main)

read_query = '''SELECT * FROM admin'''
datas = cur.execute(read_query)
for data in datas:
    print(f"ID: {data[0]} | Username: {data[1]} | Password: {data[2]}")

# sr = 'seconduser'
# search_query = '''SELECT * FROM admin WHERE username = "{sr}"'''.format(sr=sr)
# val = cur.execute(search_query)
# for data in val:
#     print(data[0], data[1], data[2])

# conn = sqlite3.connect('hotels.db')
# cur = conn.cursor()

# read_query = '''SELECT * FROM hotels'''
# val = cur.execute(read_query)
# for data in val:
    # print(data[0], data[1], data[2], data[3], data[4], data[5][:40])
    # print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]} | {data[5][:40]}")

conn.commit()
conn.close()