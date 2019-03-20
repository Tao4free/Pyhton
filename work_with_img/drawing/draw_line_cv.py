#!/use/local/bin/python3
# refer: https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html 
#        https://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-get-image-size

import numpy as np
import cv2

#from PIL import Image, ImageDraw
#im_2 = Image.open("sample.jpg")
#size2 = im_2.size
#print(size2)

img = cv2.imread("sample.jpg")

height, width, channels = img.shape
print(width,height,channels)
size = (width,height) 
print(size)

cv2.line(img,(0,0),size,(255,0,0),5)

cv2.imwrite('sample_drawline_cv.jpg',img)

#draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill="white", width=3)
#del draw
#
## write to stdout
#im.save("sample_drawline.jpg", quality=90)
