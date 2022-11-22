import sqlite3

def searchHotel():
    pass

def viewHotels():
    pass

def adminLogin():
    print("\n************************* ADMIN LOGIN *************************")
    print("Enter your username and password to login as admin")
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect('admin.db')
    cur = conn.cursor()
    select_query = '''SELECT * FROM admin WHERE username = ?''',(username)
    cur.execute(select_query)
    print("found i guess?")


print("\n************************* HOTEL RECOMMENDATION SYSTEM *************************")
print("\n\n")
print("1. Search for a Hotel")
print("2. View all Hotels")
print("3. Admin Login")
print("4. Exit")

choice = int(input("\nEnter your choice: "))
if choice == 1:
    searchHotel()
elif choice == 2:
    viewHotels()
elif choice == 3:
    adminLogin()
elif choice == 4:
    exit()