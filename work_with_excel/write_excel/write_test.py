#!/usr/local/bin/python3
# refer: https://openpyxl.readthedocs.io/en/stable/optimized.html#write-only-mode 

from openpyxl import Workbook
wb = Workbook(write_only=True)
ws = wb.create_sheet()

# now we'll fill it with 100 rows x 200 columns

for irow in range(100):
    ws.append(['%d' % i for i in range(200)])
# save the file
wb.save('new_big_file.xlsx')
