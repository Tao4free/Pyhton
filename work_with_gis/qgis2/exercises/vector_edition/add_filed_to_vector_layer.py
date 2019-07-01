from PyQt4.QtCore import QVariant

#  load and validate the layer
vectorLyr = iface.activeLayer()
print vectorLyr.isValid()

#  access the layer data provider
vpr = vectorLyr.dataProvider()

# add a Python list of QgsField objects, 
# which defines the field name and type.
vpr.addAttributes([QgsField("Fack", QVariant.Double)])

# update the fields to complete the change
vectorLyr.updateFields()

