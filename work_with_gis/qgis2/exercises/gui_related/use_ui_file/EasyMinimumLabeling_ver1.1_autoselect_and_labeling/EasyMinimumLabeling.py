# --------------------------------------------------------
#    EasyMinimumLabeling - QGIS plugins
#
#    begin                : June, 2017
#    copyright            : (c) 2017 by Tao Lu
#    email                : lutao@getc.co.jp
#
#   EasyMinimumLabeling is free software and is offered 
#   without guarantee or warranty. You can redistribute it 
#   and/or modify it under the terms of version 2 of the 
#   GNU General Public License (GPL v2) as published by the 
#   Free Software Foundation (www.gnu.org).
# --------------------------------------------------------
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import resources
from EasyMinimumLabelingDialog import EasyMinimumLabelingDialog


class EasyMinimumLabeling:
    
    def __init__(self, iface):
        self.iface = iface
        #print "Until is okay"
        
    def initGui(self):
        icon = QIcon(os.path.dirname(__file__) + "/icon.png")
        self.action = QAction(icon, "Labeling in a minimum manner", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.showdialog)
        self.iface.registerMainWindowAction(self.action, "Ctrl+L") 
        self.iface.addPluginToMenu("EasyMinimumLabeling", self.action)
        self.iface.addToolBarIcon(self.action)
        
    def showdialog(self):
        dialog = EasyMinimumLabelingDialog(self.iface) 
        dialog.show()
        dialog.exec_()
        
    def unload(self):
        self.iface.unregisterMainWindowAction(self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("EasyMinimumLabeling", self.action)