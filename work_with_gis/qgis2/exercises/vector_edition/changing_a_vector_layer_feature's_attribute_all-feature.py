# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from PyQt4.QtCore import QVariant
#  load and validate the layer
vectorLyr = iface.activeLayer()
# print vectorLyr.isValid()

vpr = vectorLyr.dataProvider()

# Most vector data providers support editing of layer data. 
# Sometimes they support just a subset of possible editing actions. 
# Use the capabilities() function to find out what set of functionality 
# is supported
caps = vpr.capabilities()
#print caps & QgsVectorDataProvider.DeleteFeatures

fields = vpr.fields()
field_names = [field.name() for field in fields]
#print "Lb|Field" in field_name
# print field_names

# add a Python list of QgsField objects, 
# which defines the field name and type.
field_list =[
["Lb|Field", QVariant.Double, "double", 13, 6],
["Lb|X", QVariant.Double, "double", 13, 6],
["Lb|Y", QVariant.Double, "double", 13, 6],
["Lb|RA", QVariant.Double, "double", 13, 6],
["Lb|Size", QVariant.Int, "integer",5],
["Lb|hp", QVariant.String, "string", 12],
["Lb|vp", QVariant.String, "string", 12],
]

flag_caps = (caps & QgsVectorDataProvider.AddAttributes) != 0
#print flag_caps
for n in range(len(field_list)):
    #print field_list[n][0]
    flag_field_exist = field_list[n][0] in field_names
    # when field not exist and functionality supported flag_exe will be true
    flag_exe = (flag_caps == True) and (not flag_field_exist == True)
    if flag_exe:
        # add list to QgsField argument noting use *
        addField = QgsField(*field_list[n])
        
        # add field
        vpr.addAttributes([addField])
    
# update the fields to complete the change
vectorLyr.updateFields()

#Index_lbsize = vectorLyr.fieldNameIndex("Lb|Size")

vectorLyr.startEditing()    
allFeatures = vectorLyr.getFeatures()
for feature in allFeatures:
    #print feature["Elevation"]
    fields = vpr.fields()
    fet = QgsFeature(fields) #[none, none, none]
    
    feature["Lb|Field"] = feature["Elevation"]
    feature["Lb|RA"] = 0
    feature["Lb|Size"] = 7
    feature["Lb|hp"] = "Center"
    feature["Lb|vp"] = "Half"
    
    vectorLyr.updateFeature(feature)
    #Call commit to save the changes
    #vectorLyr.commitChanges()    
    
for feature in allFeatures:
    vectorLyr.changeAttributeValue(feature.id(), 2, 9)