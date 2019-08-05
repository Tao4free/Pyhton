import sys                                                               

import math, random                                                                                                                               
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF 
from PyQt5.QtCore import QSize, Qt, QTime, QTimer 
from PyQt5.QtGui import QPen, QBrush, QColor, QFontMetrics, QImage
from PyQt5.QtGui import QPainter, QRadialGradient, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget

import OpenGL.GL as gl                                                        

from Particle import Particle

class GLWidget(QOpenGLWidget):

    def __init__(self):
        # To access inherited methods that have been overridden in a class
        super().__init__() # same as super(GLWidget, self).__init__()

        x = self.width() / 2; y = self.height()
        # x = self.width() / 2; y = self.height() / 2
        self.position = QPointF(x, y)
        hue = random.randint(0, 360)
        self.particle = Particle.byXY(x, y, hue)
        # self.particle = Particle.byPosition(self.position, hue)
        self.gravity = QPointF(0.0, 0.2)

        self.animationTimer = QTimer()                    
        self.animationTimer.setSingleShot(False)          
        self.animationTimer.timeout.connect(self.animate) 
        self.animationTimer.start(20)                     

        self.setAutoFillBackground(False)
        self.setMinimumSize(960,480)
        self.setWindowTitle("Watching Fireworks with You!")

    #def initializeGL(self):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # update the background
        # bgColor = QColor(Qt.darkGray)
        # bgColor.setAlpha(100)
        painter.setBrush(QColor(50, 50, 50, 50))
        # painter.setBrush(bgColor)
        painter.drawRect(0, 0, self.width(), self.height())

        self.particle.drawPoint(painter)

        painter.end()

    def animate(self):
        self.particle.applyForce(self.gravity)
        self.particle.update()

        self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    #fmt = QSurfaceFormat()
    #fmt.setSamples(4)
    #QSurfaceFormat.setDefaultFormat(fmt)

    window = GLWidget()
    #window.setFormat(fmt)
    #window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())
