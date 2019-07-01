import os
import ConfigParser

from PyQt4 import uic
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QTextDocument, QDialogButtonBox,QPixmap


pluginPath = os.path.split(os.path.dirname(__file__))[0]
WIDGET, BASE = uic.loadUiType(
    os.path.join(pluginPath, 'ui', 'aboutdialogbase.ui'))



class AboutDialog(BASE, WIDGET):
    def __init__(self, parent=None):
        # set up a dialog GUI; After these lines, we can access all dialog widgets using self.widgetName
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        
        # read the plugin version from the metadata.txt file
        cfg = ConfigParser.SafeConfigParser()
        cfg.read(os.path.join(pluginPath, 'metadata.txt'))
        version = cfg.get('general', 'version')
        
        # plugin icon is constructed from the path to the icon file
        # and then loaded into the corresponding dialog widget
        # plugin version is displayed in the lblVersion label widget
        self.lblLogo.setPixmap(
            QPixmap(os.path.join(pluginPath, 'icons', 'freebsd_daemon.jpg')))
        self.lblVersion.setText(self.tr('Version: %s') % version)
        
        doc = QTextDocument()
        doc.setHtml(self.getAboutText())
        self.textBrowser.setDocument(doc)
        self.textBrowser.setOpenExternalLinks(True) # allow the user to open links by clicking on them
        
    def getAboutText(self):
        return self.tr(
            '<p>Select features of the specified vector layer within given '
            'radius around pre-selected reference features from the another ' 'vector layer.</p>'
            '<p>Developed as demo plugin for the "QGIS By Example" book by '
            '<a href="https://www.packtpub.com/">Packt Publishing</a>.</p>')

