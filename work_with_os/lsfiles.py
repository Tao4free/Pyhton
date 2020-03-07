import os
import time
from pprint import pprint

path = '/Users/lu.tao/Documents/python2_virtualenv'

filedict = {}
for idx, (dirpath, dirnames, filenames) in enumerate(os.walk(path), 1):
    if filenames:
        for fn in filenames:
            filepath = os.path.join(dirpath, fn)
            if os.path.isfile(filepath) and  not os.access(filepath, os.X_OK):
                ctime = time.strftime('%Y/%m/%d_%H:%M:%S', time.localtime(os.stat(filepath).st_ctime))
                filedict.update({ctime: filepath})
                # print("creation time of {}:\n    {}".format(filepath, ctime))

pprint(filedict)
# print(filedict)
