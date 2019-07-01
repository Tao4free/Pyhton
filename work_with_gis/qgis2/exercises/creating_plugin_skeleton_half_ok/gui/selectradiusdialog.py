import os

from PyQt4 import uic
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QDialogButtonBox, QDialog

from qgis.core import QgsGeometry, QgsFeatureRequest,QgsSpatialIndex
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
        
        self.btnOk =self.buttonBox.button(QDialogButtonBox.Ok)
        self.btnClose =self.buttonBox.button(QDialogButtonBox.Close)
        
        self.cmbSelectionMode.clear()
        self.cmbSelectionMode.addItem(self.tr('Create new selection'))
        self.cmbSelectionMode.addItem(self.tr('Add to current selection'))
        self.cmbSelectionMode.addItem(self.tr('Remove from current selection'))
        
        self.loadSettings()

