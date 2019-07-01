from PyQt4.QtCore import *
for layer in iface.legendInterface().layers():
    print layer.name()

layer = iface.activeLayer()

pdr= layer.dataProvider()
if not pdr.isValid():
    print "Invalid layer."

# build a list of the various attributes stored in this shapefile
attr_names = []
for field in pdr.fields():
    print field.name(), field.typeName()
    attr_names.append(field.name())
print attr_names    
    
#for feature in pdr.getFeatures(QgsFeatureRequest()):
#    print feature.attribute("Lb|Field")


