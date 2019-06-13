#!/usr/local/pyhton3

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

PATH="C:\\Users\\user\\Documents\\chrome\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver = webdriver.Chrome(executable_path=PATH)

url = "https://cloud.withgoogle.com/partners/?partnerTypes=SPECIALIZATION_PARTNER&sort-type=RELEVANCE"
page = requests.get(url)
contents = page.text

driver.get(url)
contents = driver.page_source

#print (page.status_code)
#print (page.headers)
#print (page.encoding)
#print (contents)

soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())

#div = soup.find_all('div', {'class':['card']})
#div = soup.find_all('div')
#div = soup.find_all('section', {'class': ['cards__container'], 'id': 'cards__container'})
div = soup.find('section', {'class': ['cards__container']})
#print(table)
#print(div.name)
#n = 0
#for x in div:
#    #print(x.attrs)
#    n = n + 1
#print(n)



