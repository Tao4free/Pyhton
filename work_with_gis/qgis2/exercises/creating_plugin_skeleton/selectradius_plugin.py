# -*- coding: utf-8 -*-
import os

from PyQt4.QtCore import (
    QLocale, QSettings, QFileInfo, QCoreApplication, QTranslator)
from PyQt4.QtGui import (QMessageBox, QAction, QIcon)

from qgis.core import QGis

from gui.aboutdialog import AboutDialog
from gui.selectradiusdialog import SelectRadiusDialog

pluginPath = os.path.dirname(__file__)


class SelectRadiusPlugin:
    def __init__(self, iface):
        # we store a reference to the QGIS interface—passedas the iface parameter—for
        # further usage so that we can access and use it from other methods
        self.iface = iface
        
        # an internationalization support is activated
        overrideLocale =QSettings().value('locale/overrideFlag', False, bool)
        if not overrideLocale:
            locale = QLocale.system().name()[:2]
        else:
            locale = QSettings().value('locale/userLocale','')
            
            
        qmPath ='{}/i18n/selectradius_{}.qm'.format(pluginPath, locale)
        
        if QFileInfo(qmPath).exists():
            self.translator = QTranslator()
            self.translator.load(qmPath)
            QCoreApplication.installTranslator(self.translator)

# Methos starts
    def initGui(self):
        ### we create a so-called action that will launch the plugin dialog
        # create a QAction instance and assign the Select byRadius label to it
        self.actionRun = QAction(
            self.tr('Select by Radius'),self.iface.mainWindow())
        #  we construct an icon for our action
        self.actionRun.setIcon(
            QIcon(os.path.join(pluginPath, 'icons','freebsd_daemon.jpg')))
        # set the tooltip text for our action
        self.actionRun.setWhatsThis(
            self.tr('Select features within given radius'))
        # set the objectName property of the action
        self.actionRun.setObjectName('SelectRadiusRun')
        
        # used to show the About dialog
        self.actionAbout = QAction(self.tr('About'),self.iface.mainWindow())
        self.actionAbout.setIcon(
            QIcon(os.path.join(pluginPath, 'icons','about.png')))
        self.actionAbout.setWhatsThis(self.tr('About Select by Radius'))
        self.actionAbout.setObjectName('SelectRadiusAbout')
        
        # add our actions to the Select by Radius submenu
        self.iface.addPluginToVectorMenu(
            self.tr('Select by Radius'), self.actionRun)
        self.iface.addPluginToVectorMenu(
            self.tr('Select by Radius'), self.actionAbout)
        self.iface.addVectorToolBarIcon(self.actionRun)
        
        # to connect actions to handlers, which will be executed when 
        # the user presses buttons or selects menu entries
        self.actionRun.triggered.connect(self.run)
        self.actionAbout.triggered.connect(self.about)
        
    def unload(self):
        self.iface.removePluginVectorMenu(
            self.tr('Select by Radius'), self.actionRun)
        self.iface.removePluginVectorMenu(
            self.tr('Select by Radius'), self.actionAbout)
        self.iface.removeVectorToolBarIcon(self.actionRun)
        
    def run(self):
        dlg = SelectRadiusDialog(self.iface)
        dlg.exec_()
        
    def about(self):
        d = AboutDialog()
        d.exec_()
    
    def tr(self, text):
        return QCoreApplication.translate('SelectRadius',text)
