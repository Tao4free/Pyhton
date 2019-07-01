"""
class CopyCoordstool(QgsMapTool):
  def __init__(self, iface):
    QgsMapTool.__init__(self, iface.mapCanvas())

    self.canvas = iface.mapCanvas()
    #self.emitPoint = QgsMapToolEmitPoint(self.canvas)
    self.iface = iface

    self.cursor = QCursor(Qt.CrossCursor)

  def activate(self):
    self.canvas.setCursor(self.cursor)

  def canvasReleaseEvent (self, event):
  
    crsSrc = self.canvas.mapRenderer().destinationCrs()
    crsWGS = QgsCoordinateReferenceSystem(4326)

    QApplication.setOverrideCursor(Qt.WaitCursor)
    x = event.pos().x()
    y = event.pos().y()
    point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
    #If Shift is pressed, convert coords to EPSG:4326
    if event.modifiers() == Qt.ShiftModifier:
        xform = QgsCoordinateTransform(crsSrc, crsWGS)
        point = xform.transform(QgsPoint(point.x(),point.y()))
    QApplication.restoreOverrideCursor()
    
    print point

    xx = str(point.x()) 
    yy = str(point.y())


    #QMessageBox.warning(self.iface.mainWindow(),xx,yy)
    clipboard = QApplication.clipboard()
    clipboard.setText(str(xx)+"\t"+str(yy))
    

mapTool = CopyCoordstool(iface)
#iface.mapCanvas().setMapTool(mapTool)
#iface.mapCanvas().unsetMapTool(mapTool)
"""

class getCoordinate(QgsMapTool):
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.iface = iface
    
    def canvasPressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        transform = self.iface.mapCanvas().getCoordinateTransform()
        startPt = transform.toMapCoordinates(x, y)
        print "start", startPt
        
    def canvasReleaseEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        transform = self.iface.mapCanvas().getCoordinateTransform()
        endPt = transform.toMapCoordinates(x, y)
        print "end", endPt


mapTool = getCoordinate(iface)
iface.mapCanvas().setMapTool(mapTool)






