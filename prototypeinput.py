import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = []

edges = []

psq = [(1,1,0),(1,-1,0),(-1,-1,0),(-1,1,0)]

ptri = [(1,0,0),(0,1,0),(-1,0,0)]

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

def setSquare():
    global verticies
    preset = input('Use Preset?(Y/N)')
    if (preset=='Y'):
        verticies=psq
        sisi()
        Square()
    elif (preset=='N'):
        N=4
        print('Masukkan 4 titik (x,y)')
        while (N > 0):
            p=inputpoint2d()
            verticies.append(p)
            N-=1
        sisi()
        Square()
    else:
        print('Wrong input')

def Square():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glBegin(GL_QUADS)
    x=0
    for vertex in verticies:
        x+=1
        x=(x%9)
        glColor3fv(colors[x])
        glVertex3fv(vertex)
    glEnd()

def setPolygon():
    global verticies
    N=input('Masukkan jumlah sudut\n')
    N=int(N)
    if (N<=1):
        N=input('Jumlah sudut harus diatas 1\n')
    while (N > 0):
        p=inputpoint2d()
        verticies.append(p)
        N-=1
    sisi()
    Polygon()

def Polygon():
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

def setTriangle():
    global verticies
    preset = input('Use Preset?(Y/N)')
    if (preset=='Y'):
        verticies=ptri
        sisi()
        Triangle()
    elif (preset=='N'):
        N=3
        print('Masukkan 3 titik (x,y)')
        while (N>0):
            p=inputpoint2d()
            verticies.append(p)
            N-=1
        sisi()
        Triangle()
    else:
        print('Wrong input')

def Triangle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glBegin(GL_TRIANGLES)
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
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    shape=input('Pilih bentuk:\n1. Polygon\n2. Segitiga\n3. Segiempat\n')
    if (shape=='1'):
        setPolygon()
    elif (shape=='2'):
        setTriangle()
    elif (shape=='3'):
        setSquare()
    else:
        print('Input salah')

    Cartesius()

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
        pygame.display.flip()
        clock.tick(60)

main()
