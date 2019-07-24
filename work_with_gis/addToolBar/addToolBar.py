#from qgis.PyQt import QtCore, QtGui, QtWidgets
from qgis.gui import QgsMessageBar

def printSth():
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
    ms = "<font color='DeepPink'> My first action! </font>"
    iface.messageBar().pushMessage("Message", ms)
    #print(ms)

toolbar = iface.addToolBar(u'My toolbar')
iface.toolButton = QToolButton()
iface.toolButton.setIcon(QIcon("C:\\Users\\user\\Documents\\favicon.ico") )
toolbar.addWidget(iface.toolButton)
iface.toolButton.clicked.connect(printSth)

