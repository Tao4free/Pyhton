#!bin/python3
# https://stackoverflow.com/questions/44593705/how-to-copy-over-an-excel-sheet-to-another-workbook-in-python

from win32com.client import Dispatch

path1 = 'C:\\Users\\user\\Documents\\lu_temp\\xxx\\sample.xlsx'
path2 = 'C:\\Users\\user\\Documents\\lu_temp\\xxx\\sample_added.xlsx'

xl = Dispatch("Excel.Application")

wb1 = xl.Workbooks.Open(Filename=path1)
wb2 = xl.Workbooks.Open(Filename=path2)

ws1 = wb1.Worksheets("sample")

for i in range(291,355):
    if (i%5 == 0):
        continue
    newname = "No." + str(i)
    print(newname)
    wsn = wb2.Worksheets.Count

    try:
        ws1.Copy(After=wb2.Worksheets(wsn))
        ws2 = wb2.Worksheets("sample")
        ws2.Name = newname
    except:
        continue

wb2.Close(SaveChanges=True)
xl.Quit()
