import sqlite3
from adminMenu import adminMenu

def adminLogin():
    print("\n************************* ADMIN LOGIN *************************\n\n")
    print("Enter your username and password to login as admin")
    username = input("Username: ")
    password = input("Password: ")

    conna = sqlite3.connect('admin.db')
    cura = conna.cursor()
    try:
        search_query = '''SELECT * FROM admin WHERE username = "{sr}"'''.format(
            sr=username)
        val = cura.execute(search_query)
        # temp = val[0]
        for data in val:
            if data[2] == password:
                print("Login successful")
                adminMenu()
                conna.commit()
                conna.close()
            else:
                print("Incorrect password")
                adminLogin()
    except Exception as e:
        print("Error, ", e)
    adminLogin()