#!/usr/bin/python3.4
# coding:utf-8

from openpyxl import Workbook
import codecs
import time
import csv
import os
import share
from datetime import date, timedelta
import excel2csv


# Definite the start time
start_time = time.time()



share.dataitem_path = '.'

file_path = '地下水温測定結果.xlsx'
# Excek2csv
sheets = excel2csv.get_all_sheets(file_path)
excel2csv.csv_from_excel(file_path, sheets)
    


print ("")
print ("-------------------- Download is completed --------------------")
print ("-------------------- %s seconds --------------------" % (time.time() - start_time))


