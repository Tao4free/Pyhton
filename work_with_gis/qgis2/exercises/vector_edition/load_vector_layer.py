#layer = QgsVectorLayer(data_source, layer_name, provider_name)
v_1 =QgsVectorLayer('LineString', 'label_test' , "memory")

print v_1.isValid()

# add layer to layer panel
QgsMapLayerRegistry.instance().addMapLayers([v_1])

















