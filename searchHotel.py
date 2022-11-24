import sqlite3

def searchHotel():
    con2 = sqlite3.connect('hotels.db')
    curr = con2.cursor()

    print("\n")
    print("-----------------------------------------------------------------------------------------------")
    print("To search for hotel: ")
    print("On what basis would you like to search the hotel? Choose one from the following options:")
    print("1.Name")
    print("2.Price")
    print("3.Rating")
    print("4.Location")
    print("5.Exit")
    selection = int(input("Choose one of the options from above ie 1,2,3,4,5: "))

    if selection == 1:
        hname = input("Enter the name of the hotel whose details you want to see: ").lower()
        #search_comm='''SELECT * FROM  hotels where name like 'hname%' '''
        #search_comm='''SELECT * FROM  hotels where name = hname '''
        try:
            search_comm = '''SELECT * FROM hotels'''
            querdata = curr.execute(search_comm)
            for entry in querdata:
                if entry[1].lower() in hname:
                    print(entry[0], '|', entry[1], '| $', entry[2], '|', entry[3], '|', entry[4], '|', entry[5][:60])
                    return
        except:
            print("Eror in displaying the values")
            searchHotel()
        print("No such hotel found")
        searchHotel()

    if selection == 2:
        lprange = int(input("Enter the lower price range($): "))
        hprange = int(input("Enter the higher price range($): "))
        # chalena yesari
        #search_comm='''SELECT * FROM hotels where price between lprange and hprange'''
        try:
            search_comm = '''SELECT * FROM hotels'''
            querdata = curr.execute(search_comm)
            for entry in querdata:
                if entry[2] > lprange and entry[2] < hprange:
                    print(entry[0], '|', entry[1], '| $', entry[2], '|', entry[3], '|', entry[4], '|', entry[5][:60], '..')
        except:
            print("Eror in displaying the values")
            searchHotel()

    if selection == 3:
        lratrange = float(input("Enter the lower rating range: "))
        hratrange = float(input("Enter the higher rating range: "))
        # search_comm='''SELECT * FROM hotels where float(rating) between lratrange and hratrange'''
        try:
            search_comm = '''SELECT * FROM hotels'''
            querdata = curr.execute(search_comm)
            for entry in querdata:
                if float(entry[3]) >= lratrange and float(entry[3]) <= hratrange:
                    print(entry[0], '|', entry[1], '| $', entry[2], '|', entry[3], '|', entry[4], '|', entry[5][:60])
        except:
            print("Eror in displaying the values")
            searchHotel()
    

    if selection == 4:
        desloc = input("Enter the location of the hotel you want displayed: ").lower()
        # yesari ni chalena
        #search_comm='''SELECT * FROM  hotels where location like 'desloc%' '''
        try:
            search_comm = '''SELECT * FROM hotels'''
            querdata = curr.execute(search_comm)
            for entry in querdata:
                if desloc in entry[4].lower():
                    print(entry[0], '|', entry[1], '| $', entry[2], '|', entry[3], '|', entry[4], '|', entry[5][:60])
        except Exception as e:
            print("Eror in displaying the values, ", e)
            searchHotel()

    if selection == 5:
        return
    
    curr.close()
    searchHotel()