# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EasyMinimumLabeling_ver2.0_seperate.ui'
#
# Created: Sun Jun 11 13:41:25 2017
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
        Dialog.resize(900, 372)
        self.lbY = QtGui.QLabel(Dialog)
        self.lbY.setGeometry(QtCore.QRect(620, 261, 31, 41))
        self.lbY.setObjectName(_fromUtf8("lbY"))
        self.lbClick = QtGui.QLabel(Dialog)
        self.lbClick.setGeometry(QtCore.QRect(10, 200, 581, 101))
        self.lbClick.setObjectName(_fromUtf8("lbClick"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(530, 320, 331, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.pbnGetcoordinate = QtGui.QPushButton(Dialog)
        self.pbnGetcoordinate.setGeometry(QtCore.QRect(180, 310, 211, 51))
        self.pbnGetcoordinate.setObjectName(_fromUtf8("pbnGetcoordinate"))
        self.lbPoint = QtGui.QLabel(Dialog)
        self.lbPoint.setGeometry(QtCore.QRect(620, 140, 261, 51))
        self.lbPoint.setObjectName(_fromUtf8("lbPoint"))
        self.lbField = QtGui.QLabel(Dialog)
        self.lbField.setGeometry(QtCore.QRect(20, 60, 881, 81))
        self.lbField.setObjectName(_fromUtf8("lbField"))
        self.lbX = QtGui.QLabel(Dialog)
        self.lbX.setGeometry(QtCore.QRect(620, 220, 31, 31))
        self.lbX.setFrameShape(QtGui.QFrame.NoFrame)
        self.lbX.setObjectName(_fromUtf8("lbX"))
        self.cbField = QtGui.QComboBox(Dialog)
        self.cbField.setGeometry(QtCore.QRect(100, 140, 221, 51))
        self.cbField.setObjectName(_fromUtf8("cbField"))
        self.txX = QtGui.QLineEdit(Dialog)
        self.txX.setGeometry(QtCore.QRect(670, 220, 221, 41))
        self.txX.setObjectName(_fromUtf8("txX"))
        self.txY = QtGui.QLineEdit(Dialog)
        self.txY.setGeometry(QtCore.QRect(670, 270, 221, 41))
        self.txY.setObjectName(_fromUtf8("txY"))
        self.lbLayer = QtGui.QLabel(Dialog)
        self.lbLayer.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.lbLayer.setObjectName(_fromUtf8("lbLayer"))
        self.txLayer = QtGui.QLineEdit(Dialog)
        self.txLayer.setGeometry(QtCore.QRect(190, 20, 671, 41))
        self.txLayer.setObjectName(_fromUtf8("txLayer"))
        self.pbnGenerate = QtGui.QPushButton(Dialog)
        self.pbnGenerate.setGeometry(QtCore.QRect(360, 140, 161, 51))
        self.pbnGenerate.setObjectName(_fromUtf8("pbnGenerate"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "EasyMinimumLabeling", None))
        self.lbY.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Y</p></body></html>", None))
        self.lbClick.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">2. Click &quot;getCoordinate&quot; and click on canvas </span></p><p align=\"center\"><span style=\" font-size:10pt;\">where you want to put the Label</span></p></body></html>", None))
        self.pbnGetcoordinate.setText(_translate("Dialog", "getCoordinate", None))
        self.lbPoint.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">The point you click</span></p></body></html>", None))
        self.lbField.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1. Choose the field you want to Label, click &quot;Generate&quot; for label fields</span></p></body></html>", None))
        self.lbX.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">X</span></p></body></html>", None))
        self.lbLayer.setText(_translate("Dialog", "<html><head/><body><p>Current layer</p></body></html>", None))
        self.pbnGenerate.setText(_translate("Dialog", "Generate", None))

