#!/use/local/bin/python3
# refer: https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html 

import numpy as np
import cv2
import os

# Define start and end point
p1 = [1136, 673]
p2 = [1578, 362]
k = float(abs(p1[1] - p2[1])) / float(abs(p1[0] - p2[0]))

# Create the meteorology data folder
outfld = "output"
if not os.path.exists(outfld):
    os.mkdir(outfld)
os.system("rm -rf " + outfld + "/*")


# Loop
for i, x in enumerate(range(p2[0], p1[0]-5, -10),1):
    no = str("%03d" % i)
    print(no)

    # Open an img
    img = cv2.imread("sample.jpg")
    
    # Get the size of img
    height, width, channels = img.shape
    #print("width = %d height = %d" % (width, height))

    # Draw line 
    # to pass starting and ending coordinates of line, blue thickness 4px
    cv2.line(img, (p1[0],p1[1]), (p2[0],p2[1]), (255,0,255), 4)

    for ii, xx in enumerate(range(p2[0], p1[0]-5, -10),1):
        # Draw circle
        # to draw a circle, you need its center coordinates and radius. 
        yy = p2[1] + k * abs(p2[0] - xx)
        yy = int(yy)
        cv2.circle(img, (xx,yy), 5, (0,0,0), -1)

    # Draw circle
    # to draw a circle, you need its center coordinates and radius. 
    y = p2[1] + k * abs(p2[0] - x)
    y = int(y)
    #print(x,y)
    cv2.circle(img, (x,y), 5, (255,0,0), -1)
    
    # Write drawing to img
    outimg = outfld + "/" + "sample_" + no + ".jpg"
    cv2.imwrite(outimg,img)
