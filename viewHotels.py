import sqlite3

def viewHotels():
    con1 = sqlite3.connect('hotels.db')
    curso = con1.cursor()

    print("\n")
    print("-----------------------------------------------------------------------")
    print("For viewing of hotels")
    print("1.View all available hotels")
    print("2.View a specified number of hotels")
    print("3.View the hotels in a ordered form")
    print("4.Exit")
    selview = int(input("Enter the option you want to select ie 1,2,3: "))

    if selview == 1:
        try:
            viewcomm = '''SELECT * FROM hotels'''
            alldata = curso.execute(viewcomm)

            for ind in alldata:
                print(ind[0], '|', ind[1], '| $', ind[2], '|', ind[3], '|', ind[4], '|', ind[5][:40])
        except:
            print("Eror in displaying the values")
            viewHotels()

    if selview == 2:
        try:
            viewcomm = '''SELECT * FROM hotels'''
            alldata = curso.execute(viewcomm)
            count = 1
            totaln = int(input("Enter number of data entries: "))
            print('\n')
            for ind in alldata:
                print(ind[0], '|', ind[1], '| $', ind[2], '|', ind[3], '|', ind[4], '|', ind[5][:40])
                if count == totaln:
                    break
                count += 1
        except:
            print("Eror in displaying the values")
            viewHotels()

    if selview == 3:
        sortchoice = int(input(
            "Enter 1 to sort price in ascending order and 2 to sort in descending order"))
        try:
            if sortchoice == 1:
                viewcomm = '''SELECT * FROM hotels ORDER BY price ASC'''
            elif sortchoice == 2:
                viewcomm = '''SELECT * FROM hotels ORDER BY price DESC'''
            print('\n')
            alldata = curso.execute(viewcomm)
            for ind in alldata:
                print(ind[0], '|', ind[1], '| $', ind[2], '|', ind[3], '|', ind[4], '|', ind[5][:40])
        except:
            print("Eror in displaying the values")
            viewHotels()
    
    if selview == 4:
        return
    curso.close()
    viewHotels()