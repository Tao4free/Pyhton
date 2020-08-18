#!/usr/local/pyhton3
# https://stackoverflow.com/questions/43761185/click-see-more-till-the-end-using-selenium-python
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
# https://stackoverflow.com/questions/42476994/how-to-hide-chrome-driver-in-python
# https://stackoverflow.com/questions/19200497/python-selenium-webscraping-nosuchelementexception-not-recognized/19200889
# https://python-forum.io/Thread-bs4-output-html-content-into-a-txt-file

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Open log text file
f = open("gcpPartner.html", "w", encoding='utf-8')

# Initialization
driver = webdriver.Chrome(executable_path="./chromedriver")

# Set window position far away to hide
driver.set_window_position(-10000,0)

# Set url
url = "https://cloud.withgoogle.com/partners/?partnerTypes=SPECIALIZATION_PARTNER&sort-type=RELEVANCE"

# Get url
driver.get(url)

# Set wait time(secs) of page loading
SCROLL_PAUSE_TIME = 7

while True:
    # Get scroll height and scroll
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(height)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, " + str(height) + ");")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Get the button element and click
    #element = driver.find_elements_by_xpath("(//button[contains(@id, 'load-more-cards-button')])")
    try:
        element = driver.find_element_by_id('load-more-cards-button')
        element.click()
    except NoSuchElementException:
        break


# Get page source using soup
soup = BeautifulSoup(driver.page_source, 'html.parser')
#print(soup.prettify())

# Write to log file
f.write("%s" % soup.prettify())

