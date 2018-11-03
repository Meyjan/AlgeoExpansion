from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


import numpy as np

#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
 
DIRECTION = 1

def initGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH) #ngebagusin render hehe
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,1000/1000,0.1,100.0)
    glMatrixMode(GL_MODELVIEW) #buat jalanin model-view matriks

def draw_3d ():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #inisialisasi clear screen
  
    glLoadIdentity()
    glTranslatef(0.0,0.0,-6.0)

    
    glRotatef(X_AXIS,1.0,0.0,0.0)
    glRotatef(Y_AXIS,0.0,1.0,0.0)
    glRotatef(Z_AXIS,0.0,0.0,1.0)
 
    
    glBegin(GL_QUADS)
    #SISI ATAS
    glColor3f(0.0,1.0,0.0) #hijau
    glVertex3f(1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,1.0)
    glVertex3f(1.0,1.0,1.0)

    #SISI BAWAH
    glColor3f(1.0,0.5,0.0) #oranye
    glVertex3f(1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(1.0,-1.0,-1.0)

    #SISI DEPAN
    glColor3f(1.0,0.0,0.0) #MERAH
    glVertex3f(1.0,1.0,1.0)
    glVertex3f(-1.0,1.0,1.0)
    glVertex3f(-1.0,-1.0,1.0)
    glVertex3f(1.0,-1.0,1.0)

    #SISI BELAKANG
    glColor3f(1.0,1.0,0.0) #kuning
    glVertex3f(1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,1.0,-1.0)
    glVertex3f(1.0,1.0,-1.0)

    #SISI KIRI
    glColor3f(0.0,0.0,1.0) #BIRU
    glVertex3f(-1.0,1.0,1.0)
    glVertex3f(-1.0,1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,1.0)

    #SISI KANAN
    glColor3f(1.0,0.0,1.0) #MAGENTA
    glVertex3f(1.0,1.0,-1.0)
    glVertex3f(1.0,1.0,1.0)
    glVertex3f(1.0,-1.0,1.0)
    glVertex3f(1.0,-1.0,-1.0)

    glEnd()

    X_AXIS = X_AXIS - 0.30
    Z_AXIS = Z_AXIS - 0.30
    Y_AXIS = Y_AXIS - 0.30
    glutSwapBuffers() #double buffering


glutInit();
glutInitDisplayMode(GLUT_DOUBLE)
glutInitWindowSize(1000,1000)
glutInitWindowPosition(50,50)
glutCreateWindow("3D coi")
glutDisplayFunc(draw_3d)
glutIdleFunc(draw_3d)
initGL()
glutMainLoop()
