#!/usr/local/bin/python3
# refer: https://stackoverflow.com/questions/44593705/how-to-copy-over-an-excel-sheet-to-another-workbook-in-python

import os
#from openpyxl import load_workbook
from win32com.client import Dispatch
#import win32com.client as win32

xl = Dispatch("Excel.Application")
#xl.Visible = True
#xl = win32.gencache.EnsureDispatch('Excel.Application')
#xl.Visible = True

outdir = "output"
if not os.path.exists(outdir):
    os.makedirs(outdir)

#indir = "./input"
#inf_path = indir + '/' + "sample.xlsx"
#inf_path = 'C:\\cygwin64\\home\\user\\git\\Python\\work_with_excel\\copy_sheet\\sample.xlsx'
inf_path = 'C:\\Users\\user\\Documents\\lu_temp\\xxx\\sample.xlsx'

#wb = load_workbook(filename=inf_path)
#ws = wb["sample"]
#ws2 = wb.copy_worksheet(ws)
#ws2.title = "No.286"
#wb.save(inf_path)

wb = xl.Workbooks.Open(Filename=inf_path)
#wb = OpenWordbook(xl, inf_path)
#ws = wb.Worksheets("sample")
ws = wb.Worksheets(2)
ws.Copy(After=wb.Worksheets())
wb.Close(SaveChanges=True)
xl.Quit()

#for inf in infiles:
#    #print(inf)
#    inf_path = indir + "/" + inf
#
#    wb = load_workbook(filename=inf_path, read_only=True, data_only=True)
#    
#    for sheet in wb.worksheets:
#        title = sheet.title
#        mxrow = sheet.max_row
#        print(inf, " | ", title)#,mxrow)
#        
#        of = outdir + '/' + title + '.txt'
#        f = open(of, 'w')
#    
#        for nrow in range(4,mxrow):
#            #print(irow)
#            for ncol in range(3,6):
#                cellValue = sheet.cell(row=nrow, column=ncol).value
#                if cellValue == None:
#                    break
#                else:
#                    cellValue = round(cellValue, 4)
#                if ncol == 3:
#                    #print("{0:10.2f}".format(cellValue), end='')
#                    cellValue = '%.2f' % cellValue
#                    str1 = str(cellValue)
#                if ncol == 4:
#                    #print("{0:10.3f}".format(cellValue), end='') 
#                    cellValue = '%.3f' % cellValue
#                    str2 = str(cellValue)
#                if ncol == 5:
#                    #print("{0:5d}".format(cellValue)) 
#                    cellValue = '%d' % cellValue
#                    str3 = str(cellValue)
#            line     = '{:>10s} {:>10s} {:>5s}\n'.format(str1, str2, str3)
#            f.write(line)
#    
#        f.close()
#
#    wb._archive.close()

