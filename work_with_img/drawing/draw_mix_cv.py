#!/use/local/bin/python3
# refer: https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html 

import numpy as np
import cv2

# Open an img
img = cv2.imread("sample.jpg")

# Get the size of img
height, width, channels = img.shape
print("width = %d height = %d" % (width, height))

# Draw line 
# to pass starting and ending coordinates of line, blue thickness 4px
cv2.line(img, (0,0), (width,height), (255,0,0), 4)
# red thickness 2px
cv2.line(img, (0,height), (width,0), (0,0,255), 2)

# Draw rectangle 
toplt = (int(width  * 7/16), int(height * 9/16)) 
botrt = (int(width  * 9/16), int(height * 7/16)) 
# green thickness 1 px
cv2.rectangle(img, toplt, botrt, (0,255,0), 1)

# Draw circle
# to draw a circle, you need its center coordinates and radius. 
cv2.circle(img, (447,63), 63, (0,0,255), -1)

# Draw ellipse
"""
To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation of ellipse in clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. 
"""
cv2.ellipse(img, (256,256), (100,50), -90, 0, 180, (0,255,255), -1)

# Draw polygon
"""
To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32. Here we draw a small polygon of with four vertices in yellow color.
"""
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
"""
Note
If third argument is False, you will get a polylines joining all the points, not a closed shape.
cv2.polylines() can be used to draw multiple lines. Just create a list of all the lines you want to draw and pass it to the function. All lines will be drawn individually. It is a much better and faster way to draw a group of lines than calling cv2.line() for each line.
"""

# Write drawing to img
cv2.imwrite('sample_draw_mix_cv.jpg',img)
