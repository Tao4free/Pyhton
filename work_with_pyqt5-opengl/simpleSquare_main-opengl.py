#http://winfred-lu.blogspot.com/2012/09/writing-your-first-pyqt4-opengl-program.html
#http://trevorius.com/scrapbook/uncategorized/part-1-drawing-with-pyopengl-using-moden-opengl-buffers/
#https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glClearColor.xhtml

import OpenGL.GL as gl
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QOpenGLWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

# Basic window = OpenGL window + other widgets
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = GLWidget(self)

        #self.button = QPushButton('Test', self)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.widget)
        #mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)


# OpenGL window
class GLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        #QOpenGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)
        self.setWindowTitle("Simple Square Drawing")

    # OpenGL is initialized
    def initializeGL(self):
        #glClearColor(reg, green, blue, alpha)
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)

    # Where OpenGL remenbers how many pixels it should draw
    def resizeGL(self, w, h):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        gl.glViewport(0, 0, w, h)

    # Start drawing
    def paintGL(self):
        gl.glColor3f(1.0, 0.5, 0)
        gl.glRectf(-5, -5, 5, 5)
        gl.glColor3f(1.0, 1.0, 1.0)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex3f(0, 0, 0)
        gl.glVertex3f(20, 20, 0)
        gl.glEnd()


if __name__ == '__main__':
    app = QApplication(['Yo'])
    window = MainWindow()
    window.show()
    app.exec_()
