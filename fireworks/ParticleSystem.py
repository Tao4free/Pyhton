#https://stavshamir.githueb.io/python/2018/05/26/overloading-constructors-in-python.html

import numpy as np
import random
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF
from PyQt5.QtCore import QSize, Qt, QTime, QTimer
from PyQt5.QtGui import QPen, QBrush, QColor, QFontMetrics, QImage
from PyQt5.QtGui import QPainter, QRadialGradient, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

from Particle import Particle


class Firework:
    def __init__(self, width, height, gravity):
        self.hue = random.randint(0, 360)
        x = random.randint(30, width - 30); y = height;
        self.firework = Particle.byXY(x, y, self.hue)
        self.particles = []
        # self.gravity = gravity
        self.gravity = QPointF(0, 0.2)

    def isDone(self):
        if (self.firework == None and self.particles == []):
            return True
        else:
            return False

    def shoot(self):
        if (self.firework != None):
            self.firework.applyForce(self.gravity)
            self.firework.update()

            if (self.firework.explode()):
                for i in range(100):
                    self.particles.append(Particle.byPosition(self.firework.position, self.hue))

                self.firework = None

        for i in range(len(self.particles)-1, -1, -1):
            # print(i)
            p = self.particles[i]
            # p.applyForce(self.gravity)
            p.update()
            if (p.isDead()):
                self.particles.remove(p)

    def isDead(self):
        if (self.particles == []):
            return True
        else:
            return False


if __name__ == '__main__':
    particle = Particle()
