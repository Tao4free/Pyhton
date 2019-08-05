import sys                                                               

import math, random                                                                                                                               
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF 
from PyQt5.QtCore import QSize, Qt, QTime, QTimer 
from PyQt5.QtGui import QPen, QBrush, QColor, QFontMetrics, QImage
from PyQt5.QtGui import QPainter, QRadialGradient, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget

import OpenGL.GL as gl                                                        

from ParticleSystem import Firework

class GLWidget(QOpenGLWidget):

    def __init__(self):
        # To access inherited methods that have been overridden in a class
        super().__init__() # same as super(GLWidget, self).__init__()

        x = self.width(); y = self.height()
        self.position = QPointF(x, y)
        self.gravity = QPointF(0.0, 0.2)
        self.firework = Firework(x, y, self.gravity)

        self.animationTimer = QTimer()                    
        self.animationTimer.setSingleShot(False)          
        self.animationTimer.timeout.connect(self.animate) 
        # self.animationTimer.start(20)                     
        self.animationTimer.start()                     

        self.setAutoFillBackground(False)
        self.setMinimumSize(960,480)
        self.setWindowTitle("Watching Fireworks with You!")

    #def initializeGL(self):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # update the background
        painter.setBrush(QColor(50, 50, 50, 50))
        painter.drawRect(0, 0, self.width(), self.height())

        # draw the shooted firework
        if (self.firework.firework != None):
            self.firework.firework.drawPoint(painter)

        # draw the exploded firework
        # print(len(self.firework.particles))
        # if (self.firework.firework == None):
            # self.firework.newp1.drawPoint(painter)
            # self.firework.newp2.drawPoint(painter)
        # for i in range(len(self.firework.particles) - 1, -1, -1):
        for i in range(len(self.firework.particles)):
            p = self.firework.particles[i]
            p.drawPoint(painter)

        painter.end()

    # def showEvent(self, event):
        # self.particles = self.firework.getParticles()
        # print(len(self.particles))

    def animate(self):
        self.firework.shoot()

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
