#!bin/python3
#https://stackoverflow.com/questions/11110752/export-charts-from-excel-as-images-using-python
#https://stackoverflow.com/questions/6339115/python-extra-excel-chart-series-with-win32com
#https://stackoverflow.com/questions/52428985/change-data-range-in-a-chart-using-vba
#https://stackoverflow.com/questions/41184972/python-add-data-to-existing-excel-cell-win32com

from win32com.client import Dispatch

fd = "C:\\Users\\user\\Documents\\lu_temp\\zzz\\"
path = fd + "GWL.xlsx"
#print(path)

xl = Dispatch("Excel.Application")

wb = xl.Workbooks.Open(path)

ws = wb.Worksheets("graph")
ws_rain = wb.Worksheets("rain")
#print(ws_rain.Cells(2,3).Value)

#WARNING: The following line will cause the script to discard any unsaved changes in your workbook
#Ensure to save any work before running script
#xl.DisplayAlerts = False

# Existed value of series of excel chart
series = [["case1!$C$3:$C$3001","case1!$E$3:$E$3001"],["case2!$C$3:$C$3001", "case2!$E$3:$E$3001"]]
#print(series[0][0])
#print(series[0][1])
#print(series[1][0])
#print(series[1][1])

# Loop for charts
for case, chart in enumerate(ws.ChartObjects(),1):
    # make all rain data is none
    for x in range(3,147):
        ws_rain.Cells(x,3).Value = None

    # loop for rows containing data 
    for index in range(3, 2883):  
        for i, s in enumerate(chart.Chart.SeriesCollection(), 1):
            #print(i, s.Name, s.PlotOrder)
            if (i == 1):
                # for column cahrt, copy the rain data from next column
                ws_rain.Cells(index,3).Value = ws_rain.Cells(index,4).Value
            else:
                # update the value range of line chart
                old = series[case-1][s.PlotOrder-1]
                s.Values = old.replace("3001", str(index))

        # output the chart as png   
        if (case == 1):
            png_case1 = fd + "CASE01\\" + "CASE01_" + str(index-2).zfill(4) + ".png"
            chart.Chart.Export(png_case1)
        if (case == 2):
            png_case2 = fd + "CASE02\\" + "CASE02_" + str(index-2).zfill(4) + ".png"
            chart.Chart.Export(png_case2)

wb.Close(SaveChanges=False)
#xl.Quit()
