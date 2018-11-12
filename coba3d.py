import numpy as np

from operasimatriks import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

clock = pygame.time.Clock()

suduts = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    ]

verticies = []
overticies = []

edges = [
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    ]

colors = [
    (1,1,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,1,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    ]

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )


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



def setCube():
    global verticies
    preset = input('Use Preset?(Y/N)')
    if (preset=='Y'):
        verticies=suduts
        Cube()

    elif (preset=='N'):
        N=8
        print('Masukkan 8 titik (x,y,z)')
        while (N > 0):
            p=inputpoint3d()
            verticies.append(p)
            N-=1
        Cube()
    else:
        print('Wrong input')
    global overticies
    overticies =verticies

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Cartesius():
    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    glVertex3fv((0,-500,0))
    glVertex3fv((0,500,0))
    glVertex3fv((500,0,0))
    glVertex3fv((-500,0,0))
    glVertex3fv((0,0,500))
    glVertex3fv((0,0,-500))
    glEnd()

def animate(nv):
    global verticies
    a=np.array(nv)
    b=np.array(verticies)
    delta=np.divide(np.subtract(a,b),100)

    N=100
    while (N>0):
        verticies=np.add(verticies,delta)
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1

def animaterotate(sudut,sumbu):
    global verticies
    delta=sudut/100
    N=100
    while (N>0):
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Rotate3(list(vx),delta,sumbu)
            x=v.tolist()
            nverticies.append(x)
        verticies=nverticies
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1


def operate(opr):
    if (opr=='1'):
        dx=input('Masukkan dx:\n')
        dy=input('Masukkan dy:\n')
        dz=input('Masukkan dz:\n')
        dx=int(dx)
        dy=int(dy)
        dz=int(dz)
        nverticies=[]
        for vertex in mverticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Translate3(list(vx),dx,dy,dz)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)


    elif (opr=='2'):
        k=input('Masukkan k:\n')
        k=int(k)
        nverticies=[]
        for vertex in mverticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Dilate3(list(vx),k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)


    elif (opr=='3'):
        sudut=input('Masukkan sudut perputaran:\n')
        sudut=int(sudut)
        sumbu=input('Masukkan sumbu putar\n')
        animaterotate(sudut,sumbu)

    elif(opr=='4'):
        param=input('Masukkan parameter:\n')
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Reflect3(list(vx),param)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)


    elif(opr=='5'):
        sumbu=input('Masukkan sumbu:\n')
        k1=input('Masukkan k1:\n')
        k1=float(k1)
        k2=input('Masukkan k2:\n')
        k2=float(k2)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Shear3(list(vx),sumbu,k1,k2)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)


    elif(opr=='6'):
        sumbu=input('Masukkan sumbu:\n')
        k=input('Masukkan k:\n')
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Stretch3(list(vx),sumbu,k)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)


    elif(opr=='7'):
        a=input('Masukkan a:\n')
        b=input('Masukkan b:\n')
        c=input('Masukkan c:\n')
        d=input('Masukkan d:\n')
        e=input('Masukkan e:\n')
        f=input('Masukkan f:\n')
        g=input('Masukkan g:\n')
        h=input('Masukkan h:\n')
        i=input('Masukkan i:\n')
        a=float(a)
        b=float(b)
        c=float(c)
        d=float(d)
        e=float(e)
        f=float(f)
        g=float(g)
        h=float(h)
        i=float(i)
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Custom3(list(vx),a,b,c,d,e,f,g,h,i)
            x=v.tolist()
            nverticies.append(x)
        animate(nverticies)

    elif(opr=='8'):
        n = int(input('Masukkan berapa kali multi?'))
        print('Multi ', n, ' kali START')
        nverticies=[]
        mverticies=verticies
            if (opr=='1'):
                dx=input('Masukkan dx:\n')
                dy=input('Masukkan dy:\n')
                dz=input('Masukkan dz:\n')
                dx=int(dx)
                dy=int(dy)
                dz=int(dz)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Translate3(list(vx),dx,dy,dz)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies


            elif (opr=='2'):
                k=input('Masukkan k:\n')
                k=int(k)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Dilate3(list(vx),k)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies


            elif (opr=='3'):
                sudut=input('Masukkan sudut perputaran:\n')
                sudut=int(sudut)
                sumbu=input('Masukkan sumbu putar\n')

                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Rotate3(list(vx),delta,sumbu)
                    x=v.tolist()
                    nverticies.append(x)
                mverticies=nverticies
       

            elif(opr=='4'):
                param=input('Masukkan parameter:\n')
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Reflect3(list(vx),param)
                    x=v.tolist()
                nverticies.append(x)
        

            elif(opr=='5'):
                sumbu=input('Masukkan sumbu:\n')
                k1=input('Masukkan k1:\n')
                k1=float(k1)
                k2=input('Masukkan k2:\n')
                k2=float(k2)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Shear3(list(vx),sumbu,k1,k2)
                    x=v.tolist()
                nverticies.append(x)
        

            elif(opr=='6'):
                sumbu=input('Masukkan sumbu:\n')
                k=input('Masukkan k:\n')
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Stretch3(list(vx),sumbu,k)
                    x=v.tolist()
                nverticies.append(x)


            elif(opr=='7'):
                a=input('Masukkan a:\n')
                b=input('Masukkan b:\n')
                c=input('Masukkan c:\n')
                d=input('Masukkan d:\n')
                e=input('Masukkan e:\n')
                f=input('Masukkan f:\n')
                g=input('Masukkan g:\n')
                h=input('Masukkan h:\n')
                i=input('Masukkan i:\n')
                a=float(a)
                b=float(b)
                c=float(c)
                d=float(d)
                e=float(e)
                f=float(f)
                g=float(g)
                h=float(h)
                i=float(i)
                nverticies=[]
                for vertex in mverticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Custom3(list(vx),a,b,c,d,e,f,g,h,i)
                    x=v.tolist()
                nverticies.append(x)
            else:
                print('Input salah')
            n -= 1
        animate(mverticies)

    elif(opr=='9'):
        nverticies=overticies
        animate(nverticies)

    else:
        print('Input salah')

def inputpoint3d():
    instr = input('Enter a point (x,y,z): ')
    inList = [float(n) for n in instr.split(',')]
    while (len(inList)>3):
        print('Input harus (x,y,z)')
        instr = input('Enter a point (x,y,z): ')
        inList = [float(n) for n in instr.split(',')]
    return tuple(inList)

def refresh():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cartesius()
    Cube()

    pygame.display.flip()
    clock.tick(60)

def main():
    pygame.init()

    display = (800,600)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    setCube()
    Cartesius()
    
    pygame.display.set_caption('Algeo Yeah!!!')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    op='Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n8.Multi \n9.Reset\n'

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