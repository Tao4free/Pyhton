# -*- coding: utf-8 -*-

import os

from PyQt4 import uic
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QDialogButtonBox, QDialog

from qgis.core import QgsGeometry, QgsFeatureRequest, QgsSpatialIndex
from qgis.gui import QgsMessageBar

# determine the plugin path and load the dialog GUI from the Qt Designer file
pluginPath = os.path.split(os.path.dirname(__file__))[0]
WIDGET, BASE = uic.loadUiType(
    os.path.join(pluginPath, 'ui', 'selectradiusdialogbase.ui'))


class SelectRadiusDialog(BASE, WIDGET):
    def __init__(self, iface, parent=None):
        # set up a dialog GUI; After these lines, we can access all dialog widgets using self.widgetName
        super(SelectRadiusDialog, self).__init__(parent)
        self.setupUi(self)  
        
        self.iface = iface
        
        # get references to separate buttons
        self.btnOk =self.buttonBox.button(QDialogButtonBox.Ok)
        self.btnClose=self.buttonBox.button(QDialogButtonBox.Close)
        
        # the cmbSelectionMode combobox is populated with the available selection modes
        self.cmbSelectionMode.clear()
        self.cmbSelectionMode.addItem(self.tr('Create new selection'))
        self.cmbSelectionMode.addItem(self.tr('Add to current selection'))
        self.cmbSelectionMode.addItem(self.tr('Remove from current selection'))
        
        # restore the plugin's settings from the previous run
        self.loadSettings()
        
    # loadSettings() method is called when we want to restore the plugin's settings
    def loadSettings(self):
        settings = QSettings('PacktPub', 'SelectRadius')
        self.spnRadius.setValue(settings.value('radius', 1, float))        
        self.cmbSelectionMode.setCurrentIndex(
            settings.value('selectionMode', 0, int))
    
    # saveSettings() method is used to save the current values from the widgets to the plugin settings
    def saveSettings(self):
        settings = QSettings('PacktPub', 'SelectRadius')
        
        settings.setValue('radius', self.spnRadius.value())
        settings.setValue(
            'selectionMode', 
            self.cmbSelectionMode.currentIndex())
    
    
    # is called when the user clicks on the Close button
    # save the current plugin settings and close the dialog
    def reject(self):
        self.saveSettings()
        QDialog.reject(self)
    
    
    # is called when the user clicks on the OK button
    #  check whether all the required parameters are specified
    def accept(self):
        self.saveSettings() # save the current plugin settings
        
        targetLayer = self.cmbTargetLayer.currentLayer()
        if targetLayer is None:
            self.showMessage(
                self.tr('Target layer is not set. '
                    'Please specify layer and try again,'),
                QgsMessageBar.WARNING)
            return
        
        referenceLayer = self.cmbReferenceLayer.currentLayer()
        if referenceLayer is None:
            self.showMessage(
                self.tr('Reference layer is not set. '
                    'Please specify layer and try again.'),
                QgsMessageBar.WARNING)
            return
        
        referenceFeatures = referenceLayer.selectedFeatures()
        if len(referenceFeatures) == 0:
            self.showMessage(
                self.tr('There are no reference features selected in the '
                    'reference layer. Select at least one feature and '
                    'try again.'),
                QgsMessageBar.WARNING)
            return
        
    
    def showMessage(self, message, level=QgsMessageBar.INFO):
        self.iface.messageBar().pushMessage(
            message, level, self.iface.messageTimeout())



