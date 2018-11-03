import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, 0),
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0),
    )

edges = (
    (0,1),
    (0,3),
    (2,3),
    (2,1)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,1),
    (1,1,0),
    (1,0,1),
    (0,1,1),
    (1,1,1),
    (0,0,0)
    )

v=[]

clock = pygame.time.Clock()

def Square():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_QUADS)
    x=0
    for vertex in (0,1,2,3):
        x+=1
        glColor3fv(colors[x])
        glVertex3fv(verticies[vertex])
    glEnd()

def Cartesius():
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    glVertex3fv((0,0,-500))
    glVertex3fv((0,0,500))
    glVertex3fv((0,-500,0))
    glVertex3fv((0,500,0))
    glVertex3fv((500,0,0))
    glVertex3fv((-500,0,0))
    glEnd()

def inputpoint(point):
    instr = input('Enter a point (x,y): ')
    inList = [float(n) for n in instr.split(',')]
    point = tuple(inList)


def main():
    N=input('Masukkan jumlah sudut\n')
    N=int(N)
    while (N<=1):
        N=input('Jumlah sudut harus diatas 1\n')
    while (N>0):
        p=tuple
        inputpoint(p)
        v.append(p)
        N-=1
    #hhihio
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                glTranslatef(1,0.0,0.0)
            if event.type == KEYDOWN and event.key == K_LEFT:
                glTranslatef(-1,0.0,0)
            if event.type == KEYDOWN and event.key == K_UP:
                glTranslatef(0.0,1,0)
            if event.type == KEYDOWN and event.key == K_DOWN:
                glTranslatef(0.0,-1,0)
            if event.type == KEYDOWN and event.key == K_m:
                glTranslatef(0.0,0,1)
            if event.type == KEYDOWN and event.key == K_n:
                glTranslatef(0.0,0,-1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Square()
        Cartesius()
        pygame.display.flip()
        clock.tick(60)


main()
