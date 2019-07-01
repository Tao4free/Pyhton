# Get the currently selected layer
vectorLyr = iface.activeLayer()

# access the layer data provider
vpr = vectorLyr.dataProvider()

# get the fields object
fields = vpr.fields()

# get filed names
field_names = [field.name() for field in fields]
print field_names

#  create a point geometry
pnt = QgsGeometry.fromPoint(QgsPoint(-35377.2119215,-76437.6575776))

#  create a new feature and initialize the attributes
f = QgsFeature(fields)

#  set the geometry of our new  feature
f.setGeometry(pnt)

# add features and update
vpr.addFeatures([f])
vectorLyr.updateExtents()







