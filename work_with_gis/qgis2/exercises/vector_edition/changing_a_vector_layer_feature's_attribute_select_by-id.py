from PyQt4.QtCore import QVariant
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

# define the feature IDs you want to change
fetID1 = 00 #origin is 740
fetID2 = 01

#  get the index of the fields you want to change
index_lbfield = vectorLyr.fieldNameIndex("Lb|Field")
index_lbsize = vectorLyr.fieldNameIndex("Lb|Size")

#  create the Python dictionary for the attribute index and the new value
attr1 = {index_lbfield:740, index_lbsize:7}
attr2 = {index_lbfield:740, index_lbsize:7}

# use the layer's data provider to update the fields
vpr.changeAttributeValues({fetID1:attr1, fetID2:attr2})