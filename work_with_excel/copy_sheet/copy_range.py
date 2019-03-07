#!/usr/local/bin/python3

import os
from openpyxl import load_workbook

indir = "./"
infiles = os.listdir(indir)
inf = indir + '/' + "sample_added.xlsx"
inf_ref = indir + '/' + "reference.xlsx"

wb_ref = load_workbook(filename=inf_ref, read_only=True, data_only=True)
ws_ref = wb_ref["refer"]

wb = load_workbook(filename=inf)

start_no = 286
start_dis = 57.2

for row in range(1,12):#ws_ref.max_row):
    nowrow = ws_ref.cell(row,1).value
    nextrow = ws_ref.cell(row+1,1).value
    if (nowrow is None and nextrow is None):
        break
    if ('k' in str(nowrow)):
        nowrow = str(nowrow).split('k')
        nowrow = nowrow[0]
        nowrow = float(nowrow)

        no = int( (nowrow - start_dis) / 0.2 + 286 )
        noname = "No." + str(no)

        nownum = ws_ref.cell(row,2).value
        nextnum = ws_ref.cell(row+1,2).value

        #print(nowrow, ":  ", noname, ":  ", nownum, ":  ", nextnum)

        ws = wb[noname]
        #v1 = ws.cell(9,3).value
        #v2 = ws.cell(9,4).value
        #v3 = ws.cell(9,2).value
        #print("%.2f %.3f %s" % (v1, v2, v3))

        for n in range(3, 3+nownum):
            dis = float(ws_ref.cell(row,n).value)
            dem = float(ws_ref.cell(row+1,n).value)
            if (n-2 == 1):
                dis = dis - 5
                dem = float(ws_ref.cell(row+1,n+1).value)
            if (n-2 == nownum):
                dis = dis + 5
                dem = float(ws_ref.cell(row+1,n-1).value)
            dis = round(dis,2)
            dem = round(dem,3)
            #print("num %2d %10.2f %10.3f" %  (n-2, dis, dem) )


            ws.cell(6 + n-2, 3).value = dis
            ws.cell(6 + n-2, 4).value = dem

        for m in range(7+nownum, 7+nownum+100):
             ws.cell(m, 3).value = None
             ws.cell(m, 4).value = None
                    


wb.save(inf)

print("Finish!", end='')

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

