layer = iface.activeLayer()

request = QgsFeatureRequest()
request.setFlags(request.flags() ^ QgsFeatureRequest.SubsetOfAttributes)

index = QgsSpatialIndex(layer.getFeatures(request))

pt = QgsPoint(-35319.3121627, -76397.0295696)
nearestIDs = index.nearestNeighbor(pt,1)
print len(nearestIDs)

for n in range(len(nearestIDs)):
    featureId = nearestIDs[n]
    feat = layer.getFeatures(QgsFeatureRequest().setFilterFid(featureId))
    ftr = QgsFeature()
    feat.nextFeature(ftr)
    #print ftr.attributes()
    print ftr.id()