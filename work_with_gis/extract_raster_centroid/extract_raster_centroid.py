#refer: https://gis.stackexchange.com/questions/42790/gdal-and-python-how-to-get-coordinates-for-all-cells-having-a-specific-value

from osgeo import gdal
import numpy as np

f = open('cen.txt','w')

r = gdal.Open("x.tif")
band = r.GetRasterBand(1) #bands start at one
a = band.ReadAsArray().astype(np.float)

(y_index, x_index) = np.nonzero(a > 0)
#To demonstate this compare a.shape to band.XSize and band.YSize

(upper_left_x, x_size, x_rotation, upper_left_y, y_rotation, y_size) = r.GetGeoTransform()
print upper_left_x, x_size#, x_index
print upper_left_y, y_size#, y_index

x_coords = x_index * x_size + upper_left_x + (x_size / 2) #add half the cell size
y_coords = y_index * y_size + upper_left_y + (y_size / 2) #to centre the point

print len(x_coords), len(x_index)
print len(y_coords), len(y_index)
print x_index[0],y_index[0]
print a[y_index[0],x_index[0]] 
nlen = len(x_coords)

line = 'lon,lat,value\n'
f.write(line)
for n in range(0, nlen):
    ix = x_index[n]
    iy = y_index[n]
    line = str(x_coords[n]) + ',' + str(y_coords[n]) + ',' + str(a[iy,ix])  +'\n'
    f.write(line)

f.close()
