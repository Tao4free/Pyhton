import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class RainAnimation(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rain Animation")
        self.setGeometry(50, 50, 500, 500)
        self.m_rect_rain = QtCore.QRect()

        animation = QtCore.QVariantAnimation(
            parent=self,
            startValue=QtCore.QRect(self.width() / 2, 0, 5, 30),
            endValue=QtCore.QRect(self.width() / 2, self.height() - 30, 5, 30),
            duration=5 * 1000,
            valueChanged=self.set_rect_rain,
        )
        animation.start()

    def paintEvent(self, a0):
        painter = QtGui.QPainter(self)
        # Draw a White Background
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 5, QtCore.Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.white, QtCore.Qt.SolidPattern))
        painter.drawRect(self.rect())
        # Draw the rain
        painter.setPen(QtGui.QPen(QtCore.Qt.blue, 1, QtCore.Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.blue, QtCore.Qt.SolidPattern))
        painter.drawRect(self.m_rect_rain)

    @QtCore.pyqtSlot(QtCore.QVariant)
    def set_rect_rain(self, r):
        self.m_rect_rain = r
        # print(type(r))
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = RainAnimation()
    w.show()
    sys.exit(app.exec_())
