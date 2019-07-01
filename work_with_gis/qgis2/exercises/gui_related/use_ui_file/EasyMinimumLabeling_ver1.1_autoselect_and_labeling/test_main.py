from PyQt4.QtCore import *
from PyQt4.QtGui import *
#from qgis.core import *
from ui import Ui_Dialog

class EasyMinimumLabelingDialog(QDialog, Ui_Dialog):
    
    def __init__(self, parent=None):
        # initialize EasyMinimumLabelingDialog class
        #super(FindAndReplaceDlg, self).__init__(parent)
        super(self.__class__, self).__init__(parent) # not check for 
        #QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
