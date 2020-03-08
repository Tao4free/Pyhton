import os
import time
from pprint import pprint
import shutil

path = "/c/Users/takiz/Pictures/QinDi/VUE"
path = 'TaoLU'
path = "c:\\Users\\takiz\\Pictures\\QinDi\\VUE"
path = "c:\\Users\\takiz\\Pictures\\rmQinDi"

filedict = {}
rmlist = []
for (dirpath, dirnames, filenames) in os.walk(path):
    if filenames:
        # print("\n".join(filenames))
        for fn in filenames:
            filepath = os.path.join(dirpath, fn)
            s = os.stat(filepath)
            ctime = s.st_size
            ctime = time.strftime('%Y/%m/%d_%H:%M:%S', time.localtime(s.st_ctime))
            # print(fn, s.st_size, ctime)
            if ctime in filedict:
                filepath_pre = filedict[ctime]
                # print("yes", fn)
                # print(len(filepath_pre), len(filepath))
                # print(filepath_pre, "\n", filepath)
                if len(filepath_pre) < len(filepath):
                    # print("len pre < len")
                    # print("filepath_pre: ", filepath_pre)
                    # print("filepath: ", filepath)
                    rmlist.append(filepath)
                elif len(filepath_pre) > len(filepath):
                    rmlist.append(filepath_pre)
                elif len(filepath_pre) == len(filepath):
                    if filepath_pre < filepath:
                        # print("pre < ")
                        # print("filepath_pre: ", filepath_pre)
                        # print("filepath: ", filepath)
                        rmlist.append(filepath)
            else:
                filedict.update({ctime: filepath})
            # print(fn, os.path.isfile(filepath), os.access(filepath, os.X_OK))
            # if  os.path.isfile(filepath) and  not os.access(filepath, os.X_OK):
            # ctime = time.strftime('%Y/%m/%d_%H:%M:%S', time.localtime(os.stat(filepath).st_ctime))
            # ctime = time.strftime('%Y/%m/%d_%H:%M:%S', time.localtime(os.path.getctime(filepath)))
            # print(ctime)

# pprint(filedict)
# pprint(rmlist)
rmlist = list(dict.fromkeys(rmlist))
for rml in rmlist:
    spt01 = rml.split("rmQinDi")
    spt02 = rml.split("\\")
    target = spt01[0] + "\\rmQinDi2\\" + spt02[-1]
    # # print(target)
    # # try:
    shutil.move(rml, target)
    # # except:
        # # pass
# # print(len(rmlist))
