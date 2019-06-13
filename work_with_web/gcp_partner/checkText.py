#!/usr/local/pyhton3
# -*- coding: utf8 -*-

f = open("copy.txt")
nline = len(f.readlines())
f.seek(0)

xp = -1
company = "Company"
ss = 0
#for n in range(0,nline):
for n in range(0,nline):
    line = f.readline().strip()
    if ("専門パートナー" in line):
        print(xp+1,',', company,',', ss)
        xp += 1
        ss = 0
        nn = n
    if (abs(n - nn == 1)):
        company = line.replace(',','')
    if (("star" in line) and (n != nn)):
        ss = ss + 1
    #print(xp+1, line)
    #if ("stars" in line):
    #print("専門パートナー" in line)
    #print(line)
