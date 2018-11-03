from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


import numpy as np

window = 0 
width, height = 500, 400

def draw_rect(x,y,width,height): 
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()    

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity() 
    
def drawBall (): #masih error, belom keluar di layar
        glColor3f(0.0, 1.0, 0.0)
        glTranslatef(0.0,0.0,1) 
        glutSolidSphere (0.6, 7, 7)

    
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clearscreen
    glLoadIdentity()
    refresh2d(width,height) #Inisialisasi bentuk 2D

    glColor3f(2.0,7.0,1.0)  #Warna
    draw_rect(10,10,200,200) #Input benda di (10,10) dengan size 200 x 200
    drawBall(); #rencananya bikin lingkaran

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width,height)    #Inisialisasi panjang dan lebar window
glutInitWindowPosition(0,0)     #Inisialisasi posisi window
window = glutCreateWindow("Anak Dua Ribu") #Kasih nama buat window
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
