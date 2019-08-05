#https://stavshamir.githueb.io/python/2018/05/26/overloading-constructors-in-python.html

import random
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPen, QColor


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
        height = y
        lowVel = -11 * (height / 480)
        highVel = -5 * (height / 480)
        velocity = QPointF(0, random.uniform(lowVel, highVel))
        position = QPointF(x, y) 

        return cls(velocity, position, h, True)

    @classmethod
    def byPosition(cls, position, h):
        mul = random.uniform(6, 9)
        randomVel = [random.uniform(-1, 1) * mul for i in range(2)]
        velocity = QPointF(randomVel[0], randomVel[1])
        position = QPointF(position.x(), position.y()) 

        return cls(velocity, position, h, False)

    def applyForce(self, force):
        self.acceleration += force

    def isExplode(self):
        if self.seed and self.velocity.y() > 0:
            self.lifespan = 0
            return True
        return False

    # Method to update position
    def update(self):
        # if not self.seed:
            # print("OOO_in: ", "dummy", "dummy", self.position.x(), self.position.y(), self.velocity.x(), self.velocity.y(), self.acceleration.x(), self.acceleration.y())
        self.velocity += self.acceleration
        self.position += self.velocity
        if not self.seed:
            # print("OOO_ou: ", "dummy",  "dummy", self.position.x(), self.position.y(), self.velocity.x(), self.velocity.y(), self.acceleration.x(), self.acceleration.y())
            self.lifespan -= 5.0
            self.velocity *= 0.92
        self.acceleration *= 0

    # Method to display
    def display(self):
        ptColor = QColor()
        ptColor.setHsv(self.hue, 255, 255, self.lifespan)
        if self.isExplode:
            ptColor.setHsv(self.hue, 255, 255)

        # set pen
        self.pen = QPen(ptColor)
        if self.seed:
            self.pen.setWidth(4)
        else:
            self.pen.setWidth(2)

    def drawPoint(self, painter):
        painter.save() # not necessay but keep
        painter.translate(0, 0)
        painter.setPen(self.pen)
        painter.drawPoint(self.position)
        painter.restore() # not necessary but keep

    def isDead(self):
        if self.lifespan < 0.0:
            return True
        else:
            return False

if __name__ == '__main__':
    particle = Particle()
