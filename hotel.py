import sqlite3

class Hotel:
    count = 0
    def __init__(self, idval, name, price, rating, location, website, add=0, update=0, delete=0):
        self.idval = idval
        self.name = name
        self.price = price
        self.rating = rating
        self.location = location
        self.website = website
        self.add = add
        self.update = update
        self.delete = delete
        Hotel.count += 1

    @staticmethod
    def total_hotels():
        conn = sqlite3.connect('hotels.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM hotels")
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return len(rows)

    def __repr__(self):
        return f"{self.idval} | {self.name} | {self.price} | {self.rating} | {self.location} | {self.website[:50]}"

    def __len__(self):
        return Hotel.count