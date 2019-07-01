from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import QgsMapToolIdentify#, QgsMapTool
import share

class getCoordinate(QgsMapToolIdentify):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    
    def __init__(self, iface):
        QgsMapToolIdentify.__init__(self, iface.mapCanvas())
        self.iface = iface
    
    """
    def canvasPressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        transform = self.iface.mapCanvas().getCoordinateTransform()
        startPt = transform.toMapCoordinates(x, y)
        print "start", startPt
    """
        
    def canvasReleaseEvent(self, event):
        #print event.x()
        if (event.button() == Qt.LeftButton):
            x = event.pos().x()
            #sprint x
            y = event.pos().y()
            transform = self.iface.mapCanvas().getCoordinateTransform()
            self.endPt = transform.toMapCoordinates(x, y)
            share.xPosition = round(self.endPt.x(),3)
            share.yPosition = round(self.endPt.y(),3)
            share.xEvent    = x
            share.yEvent    = y
            #print self.endPt
            #print share.xPosition, share.yPosition
            self.afterLeftClick.emit()
            # Test for identify
            idf = self
            found_features = idf.identify(share.xEvent, share.yEvent, idf.TopDownStopAtFirst, idf.VectorLayer)
            if len(found_features) > 0:
                share.found_featureLayername = found_features[0].mLayer.name()
                share.found_featureID = found_features[0].mFeature.id(); # print share.found_featureID
        if (event.button() == Qt.RightButton):
            self.afterRightClick.emit()
