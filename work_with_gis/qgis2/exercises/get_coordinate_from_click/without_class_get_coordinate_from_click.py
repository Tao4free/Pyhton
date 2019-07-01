from qgis.utils import iface

feat = QgsFeature()
"""
mc = iface.mapCanvas()
layer = mc.layer(0)
provider.select()
"""
provider = layer.dataProvider()

while(provider.nextFeature(feat)):
    geometry = feat.geometry()
    print "X Coord %d: " %geometry.asPoint().x()
    print "Y Coord %d: " %geometry.asPoint().y()
    print