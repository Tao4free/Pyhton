#https://stavshamir.githueb.io/python/2018/05/26/overloading-constructors-in-python.html

import numpy as np
import random
from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF
from PyQt5.QtCore import QSize, Qt, QTime, QTimer
from PyQt5.QtGui import QPen, QBrush, QColor, QFontMetrics, QImage
from PyQt5.QtGui import QPainter, QRadialGradient, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

import OpenGL.GL as gl


class Particle:
    seed = False

    def __init__(self, velocity, position, h, seed):
        self.hue = h

        self.acceleration = QPointF(0, 0)
        self.velocity = velocity
        self.position = position
        self.seed = seed
        self.lifespan = 255.0

        self.display()

    @classmethod
    def byXY(cls, x, y, h):
        velocity = QPointF(0, random.uniform(-12, -5))
        position = QPointF(x, y) 

        return cls(velocity, position, h, True)

    @classmethod
    def byPosition(cls, position, h):
        # mul = random.uniform(4, 8)
        mul = 1
        randomVel = [random.uniform(-1, 1) * mul for i in range(2)]
        velocity = QPointF(randomVel[0], randomVel[1])
        # print("velocity", velocity.x(), velocity.y())
        position = position
        # print("position", position.x(), position.y())

        return cls(velocity, position, h, False)

    def applyForce(self, force):
        self.acceleration += force

    def explode(self):
        if (self.seed and self.velocity.y() > 0):
            self.lifespan = 0
            return True
        return False

    # Method to update position
    def update(self):
        # print(self.velocity, self.position)
        self.velocity += self.acceleration
        self.position += self.velocity
        if (not self.seed):
            self.lifespan -= 5.0
            self.velocity *= 1.0
        self.acceleration *= 0

    # Method to display
    def display(self):
        ptColor = QColor()
        # ptColor.setHsv(self.hue, 255, 255, self.lifespan)
        ptColor.setHsv(self.hue, 255, 255)
        if (self.explode):
            ptColor.setHsv(self.hue, 255, 255)

        # set pen
        self.pen = QPen(ptColor)
        if (self.seed):
            self.pen.setWidth(4)
        else:
            self.pen.setWidth(4)

    def drawPoint(self, painter):
        painter.save()
        painter.translate(0, 0)
        painter.setPen(self.pen)
        painter.drawPoint(self.position)
        painter.restore()

    def isDead(self):
        if (self.lifespan < 0.0):
            return True
        else:
            return False

if __name__ == '__main__':
    particle = Particle()
