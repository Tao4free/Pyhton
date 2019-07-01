layer = iface.activeLayer()

point = QgsPoint(-35322.2302311, -76396.2171528)
radius = 100
rect = QgsRectangle(point.x() - radius,
                    point.y() - radius,
                    point.x() + radius,
                    point.y() + radius)
                    
layer.selectByRect(rect,SetSelection)

selection = layer.selectedFeatures()
print len(selection)
for feature in selection:
    print feature.id()# do whatever you need with the feature