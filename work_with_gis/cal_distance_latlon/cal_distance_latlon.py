#!/usr/local/bin/python3
#refer: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
#       https://andrew.hedges.name/experiments/haversine/

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1_d = 52.2296756
lon1_d = 21.0122287
lat2_d = 52.406374
lon2_d = 16.9251681
lat1 = radians(lat1_d)
lon1 = radians(lon1_d)
lat2 = radians(lat2_d)
lon2 = radians(lon2_d)

print("Calculate distance from (%f,%f) to (%f,%f)" % (lat1_d,lon1_d,lat2_d,lon2_d))

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c


print("Result:", distance)
print("Should be: %10.3f km" % distance)
