#https://stackoverflow.com/questions/33201384/pyqt-opengl-drawing-simple-scenes
# example codes in pyqt5

from PyQt5.QtCore import QPoint, QPointF, QRect, QRectF
from PyQt5.QtCore import QSize, Qt, QTime, QTimer
from PyQt5.QtGui import QBrush, QColor, QFontMetrics, QImage
from PyQt5.QtGui import QPainter, QRadialGradient, QSurfaceFormat
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QWidget
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

import OpenGL.GL as gl

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = GLWidget(self)

        #self.button = QPushButton('Test', self)
        #mainLayout = QHBoxLayout()
        #mainLayout.addWidget(self.widget)
        #mainLayout.addWidget(self.button)
        #self.setLayout(mainLayout)


class GLWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        #QOpenGLWidget.__init__(self, parent)

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

        self.setMinimumSize(640, 480)
        self.setWindowTitle("Drawing Triangle Mainly Painted by PyQt")

    # OpenGL is initialized
    def initializeGL(self):
        #gl.glMatrixMode(gl.GL_MODELVIEW)
        c = self.trolltechPurple.darker()
        gl.glClearColor(c.redF(), c.greenF(), c.blueF(), c.alphaF())

    # Where OpenGL remenbers how many pixels it should draw
    def resizeGL(self, w, h):
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        #gl.glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        gl.glOrtho(-20, 20, -20, 20, -10.0, 100.0)
        gl.glViewport(0, 0, w, h)
        #gl.glViewport(50, 50, w, h)
        #w1 = int(w * 2); h1 = int(h * 2)
        #print("-------", type(h))
        #gl.glViewport(0, 0, w1, h1)

    def paintEvent(self, event):
        #self.makeCurrent()

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glPushMatrix()

        #gl.glShadeModel(gl.GL_SMOOTH)
        #gl.glEnable(gl.GL_DEPTH_TEST)
        #gl.glEnable(gl.GL_LIGHTING)
        #gl.glEnable(gl.GL_LIGHT0)
        #gl.glEnable(gl.GL_MULTISAMPLE)
        #gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION,
        #       (0.5, 5.0, 7.0, 1.0))

        #gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        #gl.glTranslatef(-3.5, 0.5, -5.0)
        #gl.glTranslatef(0.0, 0.0, 0.0)
        gl.glColor3f( 1.0, 0.5, 0.0 );
        #gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL);

        gl.glBegin(gl.GL_TRIANGLES)
        gl.glVertex3f(10.0, 0.0, 0.0)
        gl.glVertex3f(0.0, 10.0, 0.0)
        gl.glVertex3f(10.0, 10.0, 0.0)
        gl.glEnd()

        gl.glMatrixMode(gl.GL_MODELVIEW)  
        gl.glPopMatrix()

        #painter = QPainter(self)
        #painter.setRenderHint(QPainter.Antialiasing)
        #painter.end()

    #def drawTriangle



if __name__ == '__main__':
    app = QApplication(['Yo'])
    window = MainWindow()
    window.show()
    app.exec_()
