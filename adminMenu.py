from hotel import Hotel
import sqlite3

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
        print("\nAdd details for the new hotel: ")
        name = input("Hotel name: ")
        price = float(input("Price ($): "))
        rating = input("Rating: ")
        location = input("Location: ")
        website = input("Website: ")

        try:
            total = Hotel.total_hotels()
            insert_query = '''INSERT OR IGNORE INTO hotels VALUES ({idval}, "{name}", {price}, "{rating}", "{location}", "{website}")'''.format(idval=total+1, name=name, price=price, rating=rating, location=location, website=website)
            curh.execute(insert_query)
            connh.commit()

            # INSERT CLASS OBJECT HERE
            newHotel = Hotel(total+1, name, price, rating, location, website, add=1)
            print("\nHotel added successfully as: ")
            print(newHotel)
            adminMenu()
        except Exception as e:
            print("Error adding hotel ", e)
        adminMenu()

    elif choice == 2:
        idval = int(input("Enter the id of the hotel to be updated: "))
        try:
            search_query = '''SELECT * FROM hotels WHERE id = {idval}'''.format(
                idval=idval)
            datas = curh.execute(search_query)
            name = ''
            price = 0.0
            rating = ''
            location = ''
            website = ''
            for data in datas:
                name = data[1]
                price = data[2]
                rating = data[3]
                location = data[4]
                website = data[5]
            print(
                "Enter new details for the hotel: (enter 'same' if the value is not to be changed: ")
            inp = input("Hotel name: ")
            name = inp if inp != 'same' else name
            inp = input("Price ($): ")
            price = inp if inp != 'same' else price
            inp = input("Rating: ")
            rating = inp if inp != 'same' else rating
            inp = input("Location: ")
            location = inp if inp != 'same' else location
            inp = input("Website: ")
            website = inp if inp != 'same' else website
            try:
                update_query = '''UPDATE hotels SET name = "{name}", price = {price}, rating = "{rating}", location = "{location}", website = "{website}" WHERE id = {idval}'''.format(
                    name=name, price=price, rating=rating, location=location, website=website, idval=idval)
                curh.execute(update_query)
                connh.commit()
                updHotel = Hotel(idval, name, price, rating, location, website, update=1)
                print("\nHotel updated successfully as: ")
                print(updHotel)
                adminMenu()
            except Exception as e:
                print("Error updating hotel ", e)
                adminMenu()
        except Exception as e:
            print(f"Hotel with id {idval} not found", e)
            adminMenu()

    elif choice == 3:
        idval = int(input("Enter the id of the hotel to be deleted: "))
        try:
            search_script = '''SELECT * FROM hotels WHERE id = {idval}'''.format(idval=idval)
            datas = curh.execute(search_script)
            print("Hotel to be deleted: ")
            for data in datas:
                print(data[0], data[1], data[2], data[3], data[4], data[5][:40])
            ch = input("Are you sure you want to delete? y/n: ")
            if ch.lower() == 'y':
                try:
                    delete_script = '''DELETE FROM hotels WHERE id = {idval}'''.format(idval=idval)
                    curh.execute(delete_script)
                    connh.commit()
                    delHotel = Hotel(
                        idval, data[1], data[2], data[3], data[4], data[5], delete=1)
                    print("\nHotel deleted successfully!")
                    adminMenu()
                except:
                    print("Error deleting hotel!")
                    adminMenu()
        except Exception as e:
            print(f"Hotel with id {idval} not found!, ", e)
            adminMenu()

    elif choice == 4:
        print("Logging out...")
        exit()
    else:
        print("Invalid choice")
        adminMenu()
    connh.commit()
    connh.close()