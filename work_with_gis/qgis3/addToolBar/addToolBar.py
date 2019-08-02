#https://qiita.com/ozo360/items/1b8ea895be8ec6d1f5f7
#https://wiki.qt.io/Qt_for_Python_Tutorial_SimpleDialog
from qgis.PyQt import QtCore, QtGui, QtWidgets
from qgis.gui import QgsMessageBar
from qgis.PyQt.QtWidgets import QApplication, QWidget, QMainWindow
import sys

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



#class MyDialog(QDialog):
#    def __init__(self):
#        QDialog.__init__(self)
#        self.bar = QgsMessageBar()
#        self.bar.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Fixed )
#        self.setLayout(QGridLayout())
#        self.layout().setContentsMargins(0, 0, 0, 0)
#        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok)
#        self.buttonbox.accepted.connect(self.run)
#        self.layout().addWidget(self.buttonbox, 0, 0, 2, 1)
#        self.layout().addWidget(self.bar, 0, 0, 1, 1)
#        
#        self.edit = QLineEdit("Write my name here")
#        self.button = QPushButton("Show Greetings")
#        # Create layout and add widgets
#        self.layout().addWidget(self.edit)
#        self.layout().addWidget(self.button)
#        # Add button signal to greetings slot
#        self.button.clicked.connect(self.greetings)
#        self.btn1 = QtWidgets.QPushButton("Button", self)
#        self.btn1.move(30, 50)
#
#    # Greets the user
#    def greetings(self):
#        print ("Hello %s" % self.edit.text())
#        
#    def run(self):
#        self.bar.pushMessage("Hello", "World", level=Qgis.Info)
#
#myDlg = MyDialog()
#myDlg.show()


