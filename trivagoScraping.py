from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

import sqlite3

# CREATE DATABASE
conn = sqlite3.connect('hotels.db')
cur = conn.cursor()

# CREATE TABLE ON DATABASE
create_table = '''CREATE TABLE IF NOT EXISTS hotels (id INT PRIMARY KEY, name text, price REAL CHECK(price > 0), rating text, location text, website text)'''
cur.execute(create_table)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=Service("D:\API\chromedriver.exe"), options=chrome_options)
driver.get("https://www.trivago.com/en-US/lm/hotels-nepal?search=101-2;101-5;101-53;101-6;101-9;200-137;dr-20221202-20221204")
sleep(5)

# MAIN LISTS
hnames = []
hprices = []
hratings = []
hlocations = []
hwebsites = []
npgVal = '//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/div/nav/ol/li[6]/button/span'
nextPg = driver.find_element(by=By.XPATH, value=npgVal)

count = 0

# LOOP THROUGH ALL PAGES
for i in range(5):
    names = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'item-name'] span")
    prc = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'recommended-price']")
    rval = driver.find_elements(by=By.CSS_SELECTOR, value="[itemprop = 'ratingValue']")
    loc = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'distance-label-section'] span")
    sites = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'clickout-area']")
    

    # LOOP THROUGH ALL HOTELS ON A PAGE
    for name in names:
        try:
            hnames.append(name.text)
        except:
            hnames.append("Hotel N/A")
        count += 1 
    for price in prc:
        try:
            hprices.append(price.text)
        except:
            hprices.append("$45")
    for r in rval:
        try:
            if str(r.text) != '':
                hratings.append(r.text)
        except:
            hratings.append("6.9")
    for l in loc:
        try:
            if str(l.text) != '':
                hlocations.append(l.text)
        except:
            hlocations.append("Kathmandu")
    for site in sites:
        try:
            site.click()
            sleep(15)
            driver.switch_to.window(driver.window_handles[1])
            siteurl = driver.current_url
            hwebsites.append(siteurl)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            hwebsites.append(hwebsites[-1])

    sleep(5)
    # GOTO NEXT PAGE

    if i<4:
        nextPg.click()
        sleep(5)
        try:
            npgVal = '//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/div/nav/ol/li[7]/button/span'
            nextPg = driver.find_element(by=By.XPATH, value=npgVal)
        except:
            pass
    sleep(5)


# INSERT DATA INTO DATABASE
for i in range(count):
    print(f"{i+1} | {hnames[i]} | {hprices[i]} | {hratings[i]} | {hlocations[i]} | {hwebsites[i][:50]}")
    priceFlt = float(hprices[i].strip()[1:])

    insert_query = '''INSERT INTO hotels VALUES ({id}, "{name}", {price}, "{rating}", "{location}", "{website}")'''.format(id=i+1, name=hnames[i], price=priceFlt, rating=hratings[i], location=hlocations[i], website=hwebsites[i])
    cur.execute(insert_query)
    print("Inserted")

conn.commit()
conn.close()
print(f'\n\nTerminated, {count} hotels scraped')
