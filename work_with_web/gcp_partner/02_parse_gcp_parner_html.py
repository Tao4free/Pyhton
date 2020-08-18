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
    specs = card.find('div', {'class':['card__main-body--indented']}).get_text()
    specs = specs.replace('\n', '').split(',')
    specs_num = len(specs)

    dic[company] = specs_num

# Sort by the value of dictionary
n = 0
of.write('{:<3}    {:<52}    {:<2}\n'.format('No.', 'Company', 'Stars'))
for k, v in sorted(dic.items(), key=lambda x: -x[1]):
    n += 1
    cjk_num = 0
    for s in str(k):
        if len(s.encode('utf-8')) == 3:
            cjk_num += 1 
    hyphen_num = 52 - len(k)  - cjk_num
    company_hyphen = str(k) + '-'*hyphen_num
    of.write('{}    {}    {}\n'.format(str(n).ljust(3), company_hyphen, str(v).rjust(2)))

