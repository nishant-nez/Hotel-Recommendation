# HOTEL RECOMMENDATION SYSTEM

---

A Python Project based on sqlite3 package available in python that searches and recommends the best hotel for the user's given needs from the available scraped data. Also contains an admin view for the database management.

## Installation

Hotel recommendation requires sqlite3 to run.
sqlite3 is included in standard library (since Python 2.5).

Install the dependencies if not exists

```sh
pip install sqlite3
```

Optional for data scraping with Selenium package

```sh
pip install selenium
```

## Main Menu

- Search for a Hotel
- View all available Hotels
- Admin Login
- Exit

## Search Hotel Menu

Search available hotels on basis of:

- Name
- Price
- Rating
- Location
- Exit

## View Hotel Menu

- View all available hotels
- View a specified number of hotels
- View the hotels in a ordered form
- Exit

## Admin Login

- Input username and password from user
- Check for username and password match from admin.db database
- If credentials match, view Admin Menu

## Admin Menu

- Add new hotel
- Update hotel
- Delete hotel
- Logout

## Contributors

- Nishant Khadka
- Rishav Aryal

## License

Apache License 2.0
