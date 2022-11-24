from searchHotel import searchHotel
from viewHotels import viewHotels
from adminLogin import adminLogin


if __name__ == "__main__":
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
