# refer: https://gis.stackexchange.com/questions/268250/generating-polygon-representing-rough-100km-circle-around-latitude-longitude-poi
#        https://gist.github.com/twpayne/4409500
#        https://gis.stackexchange.com/questions/52705/how-to-write-shapely-geometries-to-shapefiles

from osgeo import ogr
#import ogr
import pyproj
import utm
#import utmlocal
import json
from shapely.geometry import Point, mapping
from shapely.geometry import Polygon
from shapely.ops import transform
from functools import partial
import csv,codecs


# Open a csv file
ffac = codecs.open("input_site.csv", 'r','utf-8', 'ignore')
reader = csv.reader(ffac)
header = next(reader)


# Now convert it to a shapefile with OGR
driver = ogr.GetDriverByName('Esri Shapefile')
ds = driver.CreateDataSource('GIS_Data/Buffer_5km/Buffer_WGS84_5000m_Merge.shp')
layer = ds.CreateLayer('', None, ogr.wkbPolygon)

# Add one attribute
layer.CreateField(ogr.FieldDefn('id', ogr.OFTInteger))
defn = layer.GetLayerDefn()


# Loop for every input
for n, row in enumerate(reader,1):
    number  =       row[0]
    lat     = float(row[6]) #36.58817499
    lon     = float(row[7]) #140.6594447
    
    # Get utm zone number 
    x, y, z, l  = utm.from_latlon(lat,lon)
    #print(z,l,x,y)
    #coord = (lon,lat)
    #z, l, x, y  = utmlocal.project(coord)
    #print(z,l,x,y)
    
    # Generate spsg from utm zone number
    if(lat > 0):
        epsg_tgt = 'epsg:' + str(32600 + z)
    else:
        epsg_tgt = 'epsg:' + str(32700 + z)
    #print(epsg_tgt)
    epsg_src = 'epsg:4326'
    
    #point = Point(x, y)
    point = Point(lon, lat)
    
    # Projection change parts
    wgs84_to_aeqd = partial(
        pyproj.transform,
        pyproj.Proj(init=epsg_src),
        pyproj.Proj(init=epsg_tgt),
    )
    
    aeqd_to_wgs84 = partial(
        pyproj.transform,
        pyproj.Proj(init=epsg_tgt),
        pyproj.Proj(init=epsg_src),
    )
    
    # Change point's project
    point_transformed = transform(wgs84_to_aeqd, point)
    #print(point)
    #print(point_transformed)
    
    # Make a circle buffer
    buffer = point_transformed.buffer(5000)
    #print(len(buffer))
    
    buffer_wgs84 = transform(aeqd_to_wgs84, buffer)
    #print(json.dumps(mapping(buffer_wgs84)))
    
    # Here's an example Shapely geometry
    poly = Polygon(buffer_wgs84)
    
    ## If there are multiple geometries, put the "for" loop here
    
    # Create a new feature (attribute and geometry)
    feat = ogr.Feature(defn)
    feat.SetField('id', number)
    
    # Make a geometry, from Shapely object
    geom = ogr.CreateGeometryFromWkb(poly.wkb)
    feat.SetGeometry(geom)
    
    layer.CreateFeature(feat)
    feat = geom = None  # destroy these


# Save and close everything
ds = layer = feat = geom = None
