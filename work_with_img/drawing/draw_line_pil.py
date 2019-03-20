#!/use/local/bin/python3
# refer: https://stackoverflow.com/questions/52141592/how-to-open-an-image-in-python-3-7
#        https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

from PIL import Image, ImageDraw

im = Image.open("sample.jpg")
#im.show()

size = im.size
print(size)

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill="white", width=3)
del draw

# write to stdout
im.save("sample_drawline.jpg", quality=90)
