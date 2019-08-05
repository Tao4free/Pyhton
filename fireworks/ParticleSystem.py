#https://stavshamir.githueb.io/python/2018/05/26/overloading-constructors-in-python.html

import random

from Particle import Particle


class Firework:
    def __init__(self, width, height, gravity):
        self.hue = random.randint(0, 255)
        x = random.randint(30, width - 30); y = height
        self.firework = Particle.byXY(x, y, self.hue)
        self.particles = []
        self.gravity = gravity
        self.num = 200
        # self.newp1 = None
        # self.newp2 = None

    def isDone(self):
        if self.firework == None and self.particles == []:
            return True
        else:
            return False

    def shoot(self):
        if self.firework != None:
            self.firework.applyForce(self.gravity)
            self.firework.update()

            if self.firework.isExplode():
                # self.newp1 = Particle.byPosition(self.firework.position, self.hue)
                # print("initial: ", "dummy", 1, self.newp1.position.x(), self.newp1.position.y(), self.newp1.velocity.x(), self.newp1.velocity.y())
                # self.newp2 = Particle.byPosition(self.firework.position, self.hue)
                # print("initial: ", "dummy", 2, self.newp2.position.x(), self.newp2.position.y(), self.newp2.velocity.x(), self.newp2.velocity.y())
                for i in range(self.num):
                    newp = Particle.byPosition(self.firework.position, self.hue)
                    self.particles.append(newp)
                self.firework = None

        # if self.firework == None:
            # self.newp1.update()
            # print("update: ", "dummy", 1, self.newp1.position.x(), self.newp1.position.y(), self.newp1.velocity.x(), self.newp1.velocity.y())
            # self.newp2.update()
            # print("update: ", "dummy", 2, self.newp2.position.x(), self.newp2.position.y(), self.newp2.velocity.x(), self.newp2.velocity.y())
        for i in range(len(self.particles) - 1, -1, -1):
            p = self.particles[i]

            # test
            # for j in range(len(self.particles)):
                # print("update: ", i, j+1, p.position.x(), p.position.y(), p.velocity.x(), p.velocity.y())

            p.applyForce(self.gravity * 0.25)
            p.update()
            if (p.isDead()):
                self.particles.remove(p)

    def isDead(self):
        if self.particles == []:
            return True
        else:
            return False


if __name__ == '__main__':
    particle = Particle()
