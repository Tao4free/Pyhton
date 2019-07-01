from PyQt4.QtGui import *

# function of creating a window to open file
def analyze_shapefile():
    # let's use QGIS' graphical interface to prompt the user to select a shapefile
    filename = QFileDialog.getOpenFileName(iface.mainWindow(), 
    "Select Shapefile", "~", '*.shp')
    
    if not filename:
        print "Cancelled."
        return
       
    
    # open the selected shapefile
    registry = QgsProviderRegistry.instance()
    provider = registry.provider("ogr",filename)
    if not provider.isValid():
        print "Invalid shapefile."
        return
    
    # add layer to layer panel
    layer = QgsVectorLayer(filename, 'label_test' , "ogr")
    QgsMapLayerRegistry.instance().addMapLayers([layer])

# call the function
flag_open = 0
if flag_open:
    analyze_shapefile()

layer = iface.activeLayer()

