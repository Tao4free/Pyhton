# https://stackoverflow.com/questions/36894246/qpainterdrawpixmap-doesnt-look-good-and-has-low-quality

import sys                                                               

import math, random                                                         

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QPointF, QRect 
from PyQt5.QtGui import QPen, QBrush, QColor, QPixmap
from PyQt5.QtGui import QPainter, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget

from ParticleSystem import Firework

class GLWidget(QOpenGLWidget):

    def __init__(self):
        # To access inherited methods that have been overridden in a class
        super().__init__() # same as super(GLWidget, self).__init__()

        self.gravity = QPointF(0.0, 0.2)
        self.fireworks = []

        self.animationTimer = QTimer()                    
        self.animationTimer.setSingleShot(False)          
        self.animationTimer.timeout.connect(self.animate) 
        self.animationTimer.start()                     

        self.setAutoFillBackground(False)
        self.setMinimumSize(960,480)
        self.setWindowTitle("Watching Fireworks with You!")

        self.pixmap = QPixmap("01.jpg")
        # self.pixmap = QPixmap("watcher.jpg")

    # def resizeEvent(self, event):
        # sef

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # update the background
        painter.setBrush(QColor(50, 50, 50, 50))
        painter.drawRect(0, 0, self.width(), self.height())

        # paint the watcher
        # w = self.width() / 5
        # h = self.height() / 5
        w = self.width() / 2
        h = self.height()
        ws = 0
        hs = self.height() - h
        painter.setOpacity(0.05)
        painter.drawPixmap(QRect(ws, hs, w, h), self.pixmap)
        painter.drawPixmap(QRect(w, hs, w, h), self.pixmap)
        painter.setOpacity(1)

        # paint fireworks
        for x in range(len(self.fireworks) - 1, -1, -1):
            f = self.fireworks[x]

            # paint the shooted firework
            if (f.firework != None):
                f.firework.drawPoint(painter)

            # paint the exploded firework
            for i in range(len(f.particles)):
                p = f.particles[i]
                p.drawPoint(painter)

        painter.end()

    def addFirework(self):
        if random.random() < 0.05:
            f = Firework(self.width(), self.height(), self.gravity)
            self.fireworks.append(f)

    def animate(self):
        self.addFirework()

        for i in range(len(self.fireworks) - 1, -1, -1):
            f = self.fireworks[i]
            f.shoot()
            
            if f.isDone():
                self.fireworks.remove(f)

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fmt = QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window = GLWidget()
    window.setFormat(fmt)
    window.show()
    sys.exit(app.exec_())
