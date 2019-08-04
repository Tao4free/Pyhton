#https://stackoverflow.com/questions/33201384/pyqt-opengl-drawing-simple-scenes

import OpenGL.GL as gl
import OpenGL.GLU as glu
from PyQt5.QtWidgets import QWidget, QOpenGLWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = glWidget(self)

        #self.button = QPushButton('Test', self)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.widget)
        #mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)


class glWidget(QOpenGLWidget):
    def __init__(self, parent):
        super().__init__(parent)
        #QOpenGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)

    def initializeGL(self):
        gl.glClearDepth(1.0)              
        gl.glDepthFunc(gl.GL_LESS)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glShadeModel(gl.GL_SMOOTH)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()                    
        glu.gluPerspective(45.0,1.33,0.1, 100.0) 
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glLoadIdentity()

        gl.glTranslatef(-3.5, 0.5, -5.0)
        gl.glColor3f( 1.0, 0.5, 0.0 );
        gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL);

        gl.glBegin(gl.GL_TRIANGLES)
        gl.glVertex3f(2.0,-1.2,0.0)
        gl.glVertex3f(2.6,0.0,0.0)
        gl.glVertex3f(2.9,-1.2,0.0)
        gl.glEnd()

        gl.glFlush()



if __name__ == '__main__':
    app = QApplication(['Yo'])
    window = MainWindow()
    window.show()
    app.exec_()
