import numpy as np

from operasimatriks import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = []

overticies=[]

edges = []

psq = [(1,1,0),(1,-1,0),(-1,-1,0),(-1,1,0)]

ptri = [(1,0,0),(0,1,0),(-1,0,0)]

shape=0

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

def gamecontrol():
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
    global overticies
    overticies=verticies

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
    global overticies
    overticies=verticies

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
    global overticies
    overticies=verticies

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

def refresh():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cartesius()
    if (shape==1):
        Polygon()
    elif (shape==2):
        Triangle()
    elif (shape==3):
        Square()
    pygame.display.flip()
    clock.tick(60)

def animate(nv):
    global verticies
    a=np.array(nv)
    b=np.array(verticies)
    delta=np.divide(np.subtract(a,b),100)
    print(delta)
    N=60
    while (N>0):
        verticies=np.add(verticies,delta)
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1

def animaterotate(sudut,P2):
    global verticies
    delta=sudut/100
    N=100
    while (N>0):
        nverticies=[]
        for vertex in verticies:
            print(N)
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Rotate2(list(vx),delta,P2)
            x=v.tolist()
            nverticies.append(x)
        verticies=nverticies
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1
        print(verticies)

def operate(opr):
    if (opr=='1'):
        dx=input('Masukkan dx:\n')
        dy=input('Masukkan dy:\n')
        dx=int(dx)
        dy=int(dy)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Translate2(list(vx),dx,dy)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
        print(nverticies)
    elif (opr=='2'):
        k=input('Masukkan k:\n')
        k=int(k)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Dilate2(list(vx),k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
        print(nverticies)
    elif (opr=='3'):
        sudut=input('Masukkan sudut perputaran:\n')
        sudut=int(sudut)
        print('Masukkan titik putar\n')
        P1=inputpoint2d()
        P2=createpoint3D(P1[0],P1[1],P1[2])
        animaterotate(sudut,P2)
    elif(opr=='4'):
        param=input('Masukkan parameter:\n')
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Reflect2(list(vx),param)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
        print(nverticies)
    elif(opr=='5'):
        sumbu=input('Masukkan sumbu:\n')
        k=input('Masukkan k:\n')
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Shear2(list(vx),sumbu,k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
        print(nverticies)
    elif(opr=='6'):
        sumbu=input('Masukkan sumbu:\n')
        k=input('Masukkan k:\n')
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Stretch2(list(vx),sumbu,k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
        print(nverticies)
    elif(opr=='7'):
        nverticies=overticies
        animate(nverticies)
    else:
        print('Input salah')

def main():
    pygame.init()

    global shape

    display = (800,600)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    shape=input('Pilih bentuk:\n1. Polygon\n2. Segitiga\n3. Segiempat\n')
    shape=int(shape)
    if (shape==1):
        setPolygon()
    elif (shape==2):
        setTriangle()
    elif (shape==3):
        setSquare()
    else:
        print('Input salah')

    Cartesius()

    pygame.display.set_caption('Algeo Yeah!!!')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    op='Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Reset\n'

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_r:
                operasi=input(op)
                operate(operasi)
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
        refresh()

main()
