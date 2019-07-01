# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dock_EasyMinimumLabeling.ui'
#
# Created: Sun Jun 11 08:13:27 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(809, 422)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.lbPoint = QtGui.QLabel(self.dockWidgetContents)
        self.lbPoint.setGeometry(QtCore.QRect(520, 120, 261, 61))
        self.lbPoint.setObjectName(_fromUtf8("lbPoint"))
        self.lbField = QtGui.QLabel(self.dockWidgetContents)
        self.lbField.setGeometry(QtCore.QRect(10, 70, 781, 51))
        self.lbField.setObjectName(_fromUtf8("lbField"))
        self.cbField = QtGui.QComboBox(self.dockWidgetContents)
        self.cbField.setGeometry(QtCore.QRect(110, 150, 241, 51))
        self.cbField.setObjectName(_fromUtf8("cbField"))
        self.lbClick = QtGui.QLabel(self.dockWidgetContents)
        self.lbClick.setGeometry(QtCore.QRect(0, 180, 501, 131))
        self.lbClick.setObjectName(_fromUtf8("lbClick"))
        self.lbX = QtGui.QLabel(self.dockWidgetContents)
        self.lbX.setGeometry(QtCore.QRect(530, 180, 16, 41))
        self.lbX.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbX.setObjectName(_fromUtf8("lbX"))
        self.buttonBox = QtGui.QDialogButtonBox(self.dockWidgetContents)
        self.buttonBox.setGeometry(QtCore.QRect(440, 310, 331, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.txLayer = QtGui.QLineEdit(self.dockWidgetContents)
        self.txLayer.setGeometry(QtCore.QRect(220, 30, 561, 41))
        self.txLayer.setObjectName(_fromUtf8("txLayer"))
        self.txY = QtGui.QLineEdit(self.dockWidgetContents)
        self.txY.setGeometry(QtCore.QRect(560, 230, 231, 41))
        self.txY.setObjectName(_fromUtf8("txY"))
        self.lbY = QtGui.QLabel(self.dockWidgetContents)
        self.lbY.setGeometry(QtCore.QRect(530, 230, 16, 41))
        self.lbY.setObjectName(_fromUtf8("lbY"))
        self.txX = QtGui.QLineEdit(self.dockWidgetContents)
        self.txX.setGeometry(QtCore.QRect(560, 180, 231, 41))
        self.txX.setObjectName(_fromUtf8("txX"))
        self.lbLayer = QtGui.QLabel(self.dockWidgetContents)
        self.lbLayer.setGeometry(QtCore.QRect(30, 30, 181, 29))
        self.lbLayer.setObjectName(_fromUtf8("lbLayer"))
        self.pbnClick = QtGui.QPushButton(self.dockWidgetContents)
        self.pbnClick.setGeometry(QtCore.QRect(190, 310, 131, 41))
        self.pbnClick.setObjectName(_fromUtf8("pbnClick"))
        Dialog.setWidget(self.dockWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "DockWidget", None))
        self.lbPoint.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">The point you click</span></p></body></html>", None))
        self.lbField.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1. Choose the field you want to Label</span></p></body></html>", None))
        self.lbClick.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2. Click &quot;Click me&quot; and click on canvas </span></p><p align=\"center\"><span style=\" font-size:10pt;\">where you want to put the Label</span></p></body></html>", None))
        self.lbX.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">X</span></p></body></html>", None))
        self.lbY.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Y</p></body></html>", None))
        self.lbLayer.setText(_translate("Dialog", "Current layer", None))
        self.pbnClick.setText(_translate("Dialog", "Click me", None))

