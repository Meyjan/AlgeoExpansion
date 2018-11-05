import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = []

edges = []

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

clock = pygame.time.Clock()

def sisi():
    x=0
    y=1
    for s in verticies:
        z=(x,y)
        edges.append(z)
        x+=1
        y+=1
        y=(y%(len(verticies)))


def Square():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_POLYGON)
    x=0
    for vertex in verticies:
        x+=1
        x=(x%9)
        glColor3fv(colors[x])
        glVertex3fv(vertex)
    glEnd()

def Cartesius():
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    glVertex3fv((0,-500,0))
    glVertex3fv((0,500,0))
    glVertex3fv((500,0,0))
    glVertex3fv((-500,0,0))
    glEnd()

def inputpoint2d():
    instr = input('Enter a point (x,y): ')
    inList = [float(n) for n in instr.split(',')]
    while (len(inList)>2):
        print('Input harus (x,y)')
        instr = input('Enter a point (x,y): ')
        inList = [float(n) for n in instr.split(',')]
    inList.append(0)
    return tuple(inList)


def main():
    N=input('Masukkan jumlah sudut\n')
    N=int(N)
    while (N<=1):
        N=input('Jumlah sudut harus diatas 1\n')
    while (N>0):
        p=inputpoint2d()
        verticies.append(p)
        N-=1
    for vertex in verticies:
        print(vertex)
    sisi()
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
