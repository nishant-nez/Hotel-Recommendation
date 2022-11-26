import sqlite3
from adminMenu import adminMenu

def adminLogin():
    connadmin = sqlite3.connect('admin.db')
    curadmin = connadmin.cursor()
    print("\n************************* ADMIN LOGIN *************************\n\n")
    print("Enter your username and password to login as admin")
    username = input("Username: ")
    password = input("Password: ")

    try:
        search_query = '''SELECT * FROM admin WHERE username = "{sr}"'''.format(
            sr=username)
        val = curadmin.execute(search_query)
        for data in val:
            if data[2] == password:
                print("Login successful")
                adminMenu()
                exit()
            else:
                print("Incorrect password")
                adminLogin()
    except Exception as e:
        pass
    connadmin.close()
    exit()
