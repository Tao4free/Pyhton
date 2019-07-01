lineLayer = iface.activeLayer()
provider = lineLayer.dataProvider()

spIndex = QgsSpatialIndex() #create spatial index object

feat = QgsFeature()
fit = provider.getFeatures() #gets all features in layer

# insert features to index
while fit.nextFeature(feat):
    spIndex.insertFeature(feat)

pt = QgsPoint(-35318.8976643, -76397.941466)

# QgsSpatialIndex.nearestNeighbor (QgsPoint point, int neighbors)
nearestIds = spIndex.nearestNeighbor(pt,1) # we need only one neighbour
print nearestIds

for n in range(len(nearestIds)):
    featureId = nearestIds[0]
    fit2 = lineLayer.getFeatures(QgsFeatureRequest().setFilterFid(featureId))
    ftr = QgsFeature()
    fit2.nextFeature(ftr)
    print ftr.attributes()
    print ftr.id()