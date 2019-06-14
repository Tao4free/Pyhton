#!/usr/local/pyhton3
# -*- coding: utf8 -*-
# https://stackoverflow.com/questions/21570780/using-python-and-beautifulsoup-saved-webpage-source-codes-into-a-local-file
# https://qiita.com/shizuma/items/40f1fe4702608db40ac3
# https://pyformat.info/

import unicodedata
import collections as coll
from bs4 import BeautifulSoup
#import widen_ascii as wd

# Create output file
outf = "gcpPartnerRanking.txt"
of = open(outf, "w", encoding = "utf-8")

# Open html file
url = "gcpPartner.html"
page = open(url)
soup = BeautifulSoup(page.read(), 'html.parser')

cards = soup.find_all('div', {'class':['card']})

# Define a dictionary
dic = {}

# Loop for every card to get info
for i, card in enumerate(cards, 1):
    head = card.find("h3").get_text()
    company = head.replace('\n', '').replace(',', '')
    company = company.strip()
    nstars = card.get_text().count("star") - 1

    dic[company] = nstars
    #print("%03d    %-60s    %-5s" % (i, company, nstars))

# Sort by the value of dictionary
n = 0
#of.write("%3s    %-50s    %-5s\n" % ("No.", "Company", "Stars")) # old format
of.write('{:<3}    {:<50}    {:<5}\n'.format('No.', 'company', 'Stars'))
for k, v in sorted(dic.items(), key=lambda x: -x[1]):
    n += 1
    #of.write("%03d    %-50s    %-5s\n" % (n, str(k), str(v))) # old format
    of.write('{:3d}    {:-<50}    {:^5}\n'.format(n, str(k), str(v)))
    #print(str(k) + ": " + str(v))

