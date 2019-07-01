from osgeo import ogr
from qgis.core import *
import sys

inpath = sys.argv[1]

vlayer = inpath

provider = vlayer.dataProvider()

path = provider.dataSourceUri()

tmp = path.split("|")

path_to_shp_data = tmp[0]

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(path_to_shp_data, 1)
layer = dataSource.GetLayer()
new_field = ogr.FieldDefn("Area", ogr.OFTReal)
new_field.SetWidth(32)
new_field.SetPrecision(5) #added line to set precision
layer.CreateField(new_field)

for feature in layer:
    geom = feature.GetGeometryRef()
    area = geom.GetArea() 
    print area
    feature.SetField("Area", area)
    layer.SetFeature(feature)

dataSource = None