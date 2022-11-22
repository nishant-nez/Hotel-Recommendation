from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

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

count = 0

for i in range(4):
    names = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'item-name'] span")
    prc = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'recommended-price']")
    rval = driver.find_elements(by=By.CSS_SELECTOR, value="[itemprop = 'ratingValue']")
    loc = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'distance-label-section'] span")
    sites = driver.find_elements(by=By.CSS_SELECTOR, value="[data-testid = 'clickout-area']")
    # nextPg = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/div/nav/ol/li[6]/button/span')
    nextPg = driver.find_element(by=By.CSS_SELECTOR, value="[data-testid = 'pagination'] :last-child button span")
    # fifth = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/div/nav/ol/li[5]/button')

    # filter out the empty elements
    # names = list(filter(None, names))
    # prc = list(filter(None, prc))
    # rval = list(filter(None, rval))
    # loc = list(filter(None, loc))
    # sites = list(filter(None, sites))
    # print(len(names), len(prc), len(rval), len(loc), len(sites))

    for name in names:
        hnames.append(name.text)
    for price in prc:
        hprices.append(price.text)
    for r in rval:
        if r.text != '':
            hratings.append(r.text)
    for l in loc:
        if l.text != '':
            hlocations.append(l.text)
    for site in sites:
        site.click()
        sleep(15)
        driver.switch_to.window(driver.window_handles[1])
        siteurl = driver.current_url
        hwebsites.append(siteurl)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    nextPg.click()
    sleep(5)

for i in range(len(hnames)):
    print(i, hnames[i], hprices[i], hratings[i], hlocations[i], hwebsites[i][:20])
    # append the elements to the main lists
#     for j in range(len(names)):
#         isBot = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/main/div[3]/div[1]/div[3]/div/div/nav/ol/li[5]/button')
#         hnames.append(names[j].text)
#         hprices.append(prc[j].text)
#         hratings.append(rval[j].text)
#         hlocations.append(loc[j].text)
        
#         sites[j].click()
#         sleep(15)
#         driver.switch_to.window(driver.window_handles[1])
#         siteurl = driver.current_url
#         hwebsites.append(siteurl)
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
#         count += 1
#         print(f'{count} | {hnames[j]} | {hprices[j]} | {hratings[j]} | {hlocations[j]}')
#         print(siteurl[:100])
    # nextPg.click()
    # sleep(3)

# print('\n\nTerminated')
