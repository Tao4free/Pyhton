from PyQt4 import QtGui

from PyQt4 import QtCore


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QLineEdit()
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
    w.setPalette(palette)
    font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
    w.setFont(font)
    w.show()
    sys.exit(app.exec_())
