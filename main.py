import sqlite3
from hotel import Hotel
from admin import Admin

def searchHotel():
    pass

def viewHotels():
    pass

def adminLogin():
    print("\n************************* ADMIN LOGIN *************************")
    print("Enter your username and password to login as admin")
    username = input("Username: ")
    password = input("Password: ")

    conna = sqlite3.connect('admin.db')
    cura = conna.cursor()
    try:
        search_query = '''SELECT * FROM admin WHERE username = "{sr}"'''.format(sr=username)
        val = cura.execute(search_query)
        for data in val:
            if data[2] == password:
                print("Login successful")
                adminMenu()
            else:
                print("Incorrect password")
                adminLogin()
    except:
        print("Incorrect username")
    conna.commit()
    conna.close()

def adminMenu():
    print("\n************************* ADMIN MENU *************************")
    print("\n")
    print("1. Add new hotel")
    print("2. Update hotel")
    print("3. Delete hotel")
    print("4. Logout")

    choice = int(input("Enter your choice: "))
    connh = sqlite3.connect('hotels.db')
    curh = connh.cursor()
    if choice == 1:
        print("Add details for the new hotel: ")
        name = input("Hotel name: ")
        price = float(input("Price: "))
        rating = input("Rating: ")
        location = input("Location: ")
        website = input("Website: ")

        try:
            total = Hotel.total_hotels()
            insert_query = '''INSERT OR IGNORE INTO hotels VALUES ({id}, "{name}", {price}, "{rating}", "{location}", "{website}")'''.format(id=total+1, name=name, price=price, rating=rating, location=location, website=website)
            curh.execute(insert_query)

            # INSERT CLASS OBJECT HERE
            
            print("Hotel added successfully!")
        except:
            print("Error adding hotel")
        adminMenu()

    elif choice == 2:
        id = int(input("Enter the id of the hotel to be updated: "))
        try:
            search_query = '''SELECT * FROM hotels WHERE id = {id}'''.format(id=id)
            data = curh.execute(search_query)
            name = data[1]
            price = data[2]
            rating = data[3]
            location = data[4]
            website = data[5]
            print("Enter new details for the hotel: (enter 'same' if the value is not to be changed: ")
            inp = input("Hotel name: ")
            name = inp if inp != 'same' else name
            inp = input("Price: ")
            price = inp if inp != 'same' else price
            inp = input("Rating: ")
            rating = inp if inp != 'same' else rating
            inp = input("Location: ")
            location = inp if inp != 'same' else location
            inp = input("Website: ")
            website = inp if inp != 'same' else website
            try:
                update_query = '''UPDATE hotels SET name = "{name}", price = {price}, rating = "{rating}", location = "{location}", website = "{website}" WHERE id = {id}'''.format(name=name, price=price, rating=rating, location=location, website=website, id=id)
                curh.execute(update_query)
                print("Hotel updated successfully!")
            except:
                print("Error updating hotel")
                adminMenu()
        except:
            print(f"Hotel with id {id} not found")
            adminMenu()

    elif choice == 3:
        id = int(input("Enter the id of the hotel to be deleted: "))
        try:
            search_script = '''SELECT * FROM hotels WHERE id = {id}'''.format(id=id)
            data = curh.execute(search_script)
            print("Hotel to be deleted: ")
            print(data[0], data[1], data[2], data[3], data[4], data[5][:40])
            ch = input("Are you sure you want to delete? y/n: ")
            if ch.lower() == 'y':
                try:
                    delete_script = '''DELETE FROM hotels WHERE id = {id}'''.format(id=id)
                    curh.execute(delete_script)
                    print("Hotel deleted successfully!")
                    adminMenu()
                except:
                    print("Error deleting hotel!")
        except:
            print(f"Hotel with id{id} not found!")

    elif choice == 4:
        print("Logging out...")
        main()
    else:
        print("Invalid choice")
        adminMenu()
    curh.commit()
    curh.close()


def main():
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

main()