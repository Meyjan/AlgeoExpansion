import numpy as np

from operasimatriks import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

objects=[]

class obj:
    def __init__(self,verticies,overticies,edges,shape):
        self.v=verticies
        self.o=overticies
        self.e=edges
        self.s=shape

idx=0

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

def addobject():
    global verticies
    global edges
    global objects
    global shape
    global idx
    verticies=[]
    edges=[]
    shape=input('Pilih bentuk:\n1. Polygon\n2. Segitiga\n3. Segiempat\n4. Lingkaran\n')
    shape=int(shape)
    if (shape==1):
        setPolygon()
    elif (shape==2):
        setTriangle()
    elif (shape==3):
        setSquare()
    elif (shape==4):
        setCircle()
    else:
        print('Input salah')
    ob=obj(verticies,overticies,edges,shape)
    objects.append(ob)
    idx=len(objects)-1

def sisi():
    global edges
    x=0
    y=1
    for s in verticies:
        z=(x,y)
        edges.append(z)
        x+=1
        y+=1
        y=(y%(len(verticies)))

def highlight():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,1,1))
            glVertex3fv(verticies[vertex])
    glEnd()


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
    N=input('Masukkan jumlah sudut (Sudut-sudut yang dimasukkan harus berurutan)\n')
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
    glBegin(GL_POLYGON)
    x=0
    for vertex in verticies:
        x+=1
        x=(x%9)
        glColor3fv(colors[x])
        glVertex3fv(vertex)
    glEnd()

def setCircle():
    global verticies
    r=input('Masukkan radius\n')
    r=float(r)
    sudut=360
    while (sudut>0):
        p=(np.cos(np.deg2rad(sudut))*r,np.sin(np.deg2rad(sudut))*r,0)
        verticies.append(p)
        sudut-=1
    sisi()
    Circle()
    global overticies
    overticies=verticies

def Circle():
    glBegin(GL_POLYGON)
    x=0
    for vertex in verticies:
        x+=1
        y=((x//40)%9)
        glColor3fv(colors[y])
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
    valid=False
    TruList=[]
    while (not(valid)) or (not(len(TruList) == 2)):
        TruList=[]
        instr = input('Enter a point (x,y): ')
        inList = [n for n in instr.split(',')]
        for n in inList:
            valid=RepresentFloat(n)
            if (not(valid)):
                print('Input Salah!\n')
                break
            else:
                TruList.append(float(n))
        if (not(len(TruList) == 2)):
            print('Input harus x,y\n')
    TruList.append(0)
    print(TruList)
    return tuple(TruList)

def refresh():
    global verticies
    global edges
    global shape
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for ob in objects:
        verticies=ob.v
        edges=ob.e
        shape=ob.s
        if (shape==1):
            Polygon()
        elif (shape==2):
            Triangle()
        elif (shape==3):
            Square()
        elif (shape==4):
            Circle()
        if(ob==objects[idx]):
            highlight()
    Cartesius()
    pygame.display.flip()
    clock.tick(60)

def animate(nv):
    global verticies
    global objects
    a=np.array(nv)
    b=np.array(verticies)
    delta=np.divide(np.subtract(a,b),100)
    N=100
    while (N>0):
        verticies=np.add(verticies,delta)
        objects[idx].v=verticies
        refresh()
        gamecontrol()
        pygame.time.wait(10)
        N-=1

def animaterotate(sudut,P2):
    global verticies
    global objects
    delta=sudut/100
    N=100
    while (N>0):
        nverticies=[]
        for vertex in verticies:
            vx=createpoint2D(vertex[0],vertex[1])
            v=Rotate2(list(vx),delta,P2)
            x=v.tolist()
            nverticies.append(x)
        print(nverticies)
        verticies=nverticies
        objects[idx].v=verticies
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1

def operate(opr):
    if (opr=='1'):
        dx=input('Masukkan dx:\n')
        dy=input('Masukkan dy:\n')
        dx=float(dx)
        dy=float(dy)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Translate2(list(vx),dx,dy)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
    elif (opr=='2'):
        k=input('Masukkan k:\n')
        k=float(k)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Dilate2(list(vx),k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
    elif (opr=='3'):
        sudut=input('Masukkan sudut perputaran:\n')
        sudut=float(sudut)
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
    elif(opr=='5'):
        sumbu=input('Masukkan sumbu:\n')
        k=input('Masukkan k:\n')
        k=float(k)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Shear2(list(vx),sumbu,k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
    elif(opr=='6'):
        sumbu=input('Masukkan sumbu:\n')
        k=input('Masukkan k:\n')
        k=float(k)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Stretch2(list(vx),sumbu,k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)
    elif(opr=='7'):
        a=input('Masukkan a:\n')
        b=input('Masukkan b:\n')
        c=input('Masukkan c:\n')
        d=input('Masukkan d:\n')
        a=float(a)
        b=float(b)
        c=float(c)
        d=float(d)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Custom2(list(vx),a,b,c,d)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)

    elif(opr=='8'):
        n = int(input('Masukkan berapa kali multi?'))
        print('Multi ', n, ' kali START')
        nverticies=[]
        mverticies=verticies
        while (n>0):
            print ('Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n')
            opr = input('Masukkan operan')
            if (opr=='1'):
                dx=input('Masukkan dx:\n')
                dy=input('Masukkan dy:\n')
                dx=float(dx)
                dy=float(dy)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Translate2(list(vx),dx,dy)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif (opr=='2'):
                k=input('Masukkan k:\n')
                k=float(k)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Dilate2(list(vx),k)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif (opr=='3'):
                sudut=input('Masukkan sudut perputaran:\n')
                sudut=float(sudut)
                print('Masukkan titik putar\n')
                P1=inputpoint2d()
                P2=createpoint3D(P1[0],P1[1],P1[2])
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Rotate2(list(vx),delta,P2)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif(opr=='4'):
                param=input('Masukkan parameter:\n')
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Reflect2(list(vx),param)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif(opr=='5'):
                sumbu=input('Masukkan sumbu:\n')
                k=input('Masukkan k:\n')
                k=float(k)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Shear2(list(vx),sumbu,k)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif(opr=='6'):
                sumbu=input('Masukkan sumbu:\n')
                k=input('Masukkan k:\n')
                k=float(k)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Stretch2(list(vx),sumbu,k)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            elif(opr=='7'):
                a=input('Masukkan a:\n')
                b=input('Masukkan b:\n')
                c=input('Masukkan c:\n')
                d=input('Masukkan d:\n')
                a=float(a)
                b=float(b)
                c=float(c)
                d=float(d)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Custom2(list(vx),a,b,c,d)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
            else:
                print('Input salah')
            n -= 1
        animate(mverticies)
    elif(opr=='9'):
        nverticies=overticies
        animate(nverticies)
    else:
        print('Input salah')

def main():
    pygame.init()

    global objects
    global shape
    global idx

    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    addobject()
    Cartesius()

    pygame.display.set_caption('Algeo Yeah!!!')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    op='Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n8. Multi\n9. Reset\n'

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_r:
                operasi=input(op)
                operate(operasi)
            if event.type == KEYDOWN and event.key == K_a:
                addobject()
            if event.type == KEYDOWN and event.key == K_c:
                idx+=idx
            if event.type == KEYDOWN and event.key == K_RIGHT:
                glTranslatef(0.2,0.0,0.0)
            if event.type == KEYDOWN and event.key == K_LEFT:
                glTranslatef(-0.2,0.0,0)
            if event.type == KEYDOWN and event.key == K_UP:
                glTranslatef(0.0,0.2,0)
            if event.type == KEYDOWN and event.key == K_DOWN:
                glTranslatef(0.0,-0.2,0)
            if event.type == KEYDOWN and event.key == K_m:
                glTranslatef(0.0,0,0.2)
            if event.type == KEYDOWN and event.key == K_n:
                glTranslatef(0.0,0,-0.2)
        refresh()

main()
