from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import QgsMapTool
import share

class getCoordinate(QgsMapTool):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
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
        if (event.button() == Qt.LeftButton):
            x = event.pos().x()
            y = event.pos().y()
            transform = self.iface.mapCanvas().getCoordinateTransform()
            self.endPt = transform.toMapCoordinates(x, y)
            share.xPosition = round(self.endPt.x(),3)
            share.yPosition = round(self.endPt.y(),3)
            #print self.endPt
            #print share.xPosition, share.yPosition
            self.afterLeftClick.emit()
        if (event.button() == Qt.RightButton):
            self.afterRightClick.emit()
