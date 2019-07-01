# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         * 
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>. *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from PyQt4 import QtGui, QtCore
#from qgis.gui import QgsMapTool
import share

from ui import Ui_Dialog
from getCoordinate import getCoordinate

class EasyMinimumLabelingDialog(QDialog, Ui_Dialog):
    
    def __init__(self, iface):
        # initialize EasyMinimumLabelingDialog class
        super(self.__class__, self).__init__(None, Qt.WindowStaysOnTopHint) #QtGui.QDialog.__init__(self, None, Qt.WindowStaysOnTopHint) # another method to initialize
        self.iface = iface
        
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # prepare map tool for using defined QgsMapTool
        self.mapTool = getCoordinate(self.iface)
        
        # connect signal to function and set variable
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.write)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.write)
        self.ui.txX.setText("")#"No, I cant!")
        self.ui.txY.setText("")#"Yes, you can!")
        self.ui.txLayer.setText("")
        self.ui.cbField.clear()
        global flag_create, field_list
        flag_create = False
        field_list = []
        
        # get current layer
        layer = self.iface.mapCanvas().currentLayer() #print layer, layer.name(), layer.type() == QgsMapLayer.VectorLayer
        
        # decide the layer type and show some message to dialog
        if (layer) and layer.type() == QgsMapLayer.VectorLayer:
            if layer.type() == QgsMapLayer.VectorLayer:
                # set current layer
                self.ui.txLayer.setText(layer.name())
                # prepare to access to layer data
                vpr = layer.dataProvider()
                fields = vpr.fields()
                # show fields items for combobox
                for f in fields:
                    self.ui.cbField.addItem(f.name())
                # connect pushbutton to functions
                self.ui.pbnGenerate.clicked.connect(self.createField)
                self.ui.pbnGetcoordinate.clicked.connect(self.point)
        elif (layer) and layer.type() != QgsMapLayer.VectorLayer:
                self.ui.txLayer.setText(layer.name())
                infoString = unicode("<font color='black'> 1. </font>" + "<font color='red'> Current layer is not a vector layer</font>")
                self.ui.lbField.setText(infoString)
                self.falseSet()
        else:
            infoString = unicode("No layer selected... Select a layer from the layer list")
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            self.ui.txLayer.setPalette(palette)
            self.ui.txLayer.setText(infoString)
            self.falseSet()

     
    def falseSet(self):
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(False)
        self.ui.txX.setEnabled(False)
        self.ui.txY.setEnabled(False)
        self.ui.cbField.setEnabled(False)
        self.ui.pbnGenerate.setEnabled(False)
        self.ui.pbnGetcoordinate.setEnabled(False)

    
    def createField(self):
        # get global variable
        global flag_create, field_list
        flag_create = True
        
        # get current layer
        layer = self.iface.mapCanvas().currentLayer()
        nF = layer.selectedFeatureCount() #print nF #self.ui.txX.setText("Yes, you can!")
        # Get the field of current comobox
        lbField_origin = str(self.ui.cbField.currentText()) #print lbField_origin
        # prepare to access to layer data
        vpr = layer.dataProvider()
        # get fields and fileds' names
        fields = vpr.fields()
        field_names = [field.name() for field in fields]
        
        # add a Python list of QgsField objects, 
        # which defines the field name and type.
        lbHeader = lbField_origin[0:3]
        field_list =[
            [lbHeader + "|Field", QVariant.Double, "double", 13, 6],
            [lbHeader + "|X", QVariant.Double, "double", 13, 6],
            [lbHeader + "|Y", QVariant.Double, "double", 13, 6],
            [lbHeader + "|Rot", QVariant.Double, "double", 13, 6],
            [lbHeader + "|Size", QVariant.Int, "integer",5],
            [lbHeader + "|AlignH", QVariant.String, "string", 12],
            [lbHeader + "|AlignV", QVariant.String, "string", 12],
            ]
        #print field_list[0][0]
        
        # Most vector data providers support editing of layer data. 
        # Sometimes they support just a subset of possible editing actions. 
        # Use the capabilities() function to find out what set of functionality is supported
        # 0 means NoCapabilities
        caps = vpr.capabilities()
        flag_caps = (caps & QgsVectorDataProvider.AddAttributes) != 0
        #print flag_caps
        for n in range(len(field_list)):
            #print field_list[n][0]
            flag_field_exist = field_list[n][0] in field_names
            #print field_list[n][0]
            # when field not exist and functionality supported flag_exe will be true
            flag_exe = (flag_caps == True) and (not flag_field_exist == True)
            if flag_exe:
                # add list to QgsField argument noting use *
                addField = QgsField(*field_list[n])
                # add field
                vpr.addAttributes([addField])
                
        # update the fields to complete the change
        layer.updateFields()
        
        # start to edit attributes of fields
        layer.startEditing()    
        allFeatures = layer.getFeatures()
        for feature in allFeatures:
             fields = vpr.fields()
             #fet = QgsFeature(fields) #[none, none, none]
             feature[field_list[0][0]] = feature[lbField_origin]
             feature[field_list[1][0]] = 0.0
             feature[field_list[2][0]] = 0.0
             feature[field_list[3][0]] = 0.0
             feature[field_list[4][0]] = 9
             feature[field_list[5][0]] = "Center"
             feature[field_list[6][0]] = "Half"
             
             layer.updateFeature(feature)   
        
        # parameters for advanced labeling -- picked up from a qgs model file
        # generic labeling properties
        layer.setCustomProperty("labeling/fieldName", field_list[0][0] )
        layer.setCustomProperty("labeling","pal" ) # new gen labeling activated
        layer.setCustomProperty("labeling/fontSize","9" ) # default value
        layer.setCustomProperty("labeling/multiLineLabels","true" ) # default value
        layer.setCustomProperty("labeling/enabled","true" ) # default value
        # layer.setCustomProperty("labeling/displayAll", "true") # force all labels to display
        layer.setCustomProperty("labeling/priority", "10") # puts a high priority to labeling layer
        layer.setCustomProperty("labeling/multilineAlign","1") # multiline align to center
        # layer.setCustomProperty("labeling/wrapChar", "%") # multiline break symbol
        # line properties case
        layer.setCustomProperty("labeling/placement","4" ) 
        
        # data defined properties
        layer.setCustomProperty("labeling/dataDefined/PositionX", "1~~0~~~~" + field_list[1][0])  
        layer.setCustomProperty("labeling/dataDefined/PositionY", "1~~0~~~~" + field_list[2][0])  
        layer.setCustomProperty("labeling/dataDefined/Rotation" ,"1~~0~~~~" + field_list[3][0])
        layer.setCustomProperty("labeling/dataDefined/Size" ,"1~~0~~~~" + field_list[4][0])
        layer.setCustomProperty("labeling/dataDefined/Hali", "1~~0~~~~" + field_list[5][0])  
        layer.setCustomProperty("labeling/dataDefined/Vali","1~~0~~~~" + field_list[6][0])  

        # updateExtents and refresh mapCanvas
        layer.updateExtents()
        self.iface.mapCanvas().refresh()

        
    def point(self):
        layer = self.iface.mapCanvas().currentLayer()
        nF = layer.selectedFeatureCount()
        if (nF == 0):
            infoString = unicode("<font color='black'> 2. </font>" + "<font color='red'> Please select one element of current layer.</font>")
            self.ui.lbClick.setText(infoString)
            self.falseSet()
        elif (nF == 1):
            infoString = unicode("<font color='black'> 2. </font>" + "<font color='black'> Click 'getCoordinate' to choose a label point.</font>")
            self.ui.lbClick.setText(infoString)
            self.ui.txLayer.setText(layer.name())
            # setup QgsMapTool
            self.iface.mapCanvas().setMapTool(self.mapTool)
            # trigger to functions
            self.mapTool.afterLeftClick.connect(self.showXY)
            self.mapTool.afterRightClick.connect(self.write)
        else:
            infoString = unicode("<font color='black'> 2. </font>" + "<font color='red'> Please select only one element</font>")
            self.ui.lbClick.setText(infoString)
            self.falseSet()
                
    
    def showXY(self):
        self.ui.txX.setText(str(share.xPosition))
        self.ui.txY.setText(str(share.yPosition))

       
    def write(self):
        layer = self.iface.mapCanvas().currentLayer()
        if not flag_create:
            self.createField() #print flag_create #self.ui.txY.setText("I also think so!")
        
        # get x, y value from txX,txY qlineText and change them to attribute table
        try:
            x = float(self.ui.txX.text()); #print x
            y = float(self.ui.txY.text()); #print y
            selectFet = layer.selectedFeatures()[0]
            # get the index of the fields you want to change
            indexX = layer.fieldNameIndex(field_list[1][0])
            indexY = layer.fieldNameIndex(field_list[2][0])
            #print indexX, indexY, selectFet.attributes()
            layer.changeAttributeValue(selectFet.id(), indexX, x)
            layer.changeAttributeValue(selectFet.id(), indexY, y)
            self.iface.mapCanvas().refresh()
        except ValueError:
            QMessageBox.information(self, "Info", "Oops! getCoordinate first!", QtGui.QMessageBox.Ok)
