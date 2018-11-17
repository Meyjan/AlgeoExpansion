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

surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    ]


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
    glColor3fv((1,0,1))
    glVertex3fv((0,-500,0))
    glVertex3fv((0,500,0))
    glColor3fv((1,0,0))
    glVertex3fv((500,0,0))
    glVertex3fv((-500,0,0))
    glColor3fv((0,0,1))
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

def animaterotate(sudut,P2,sumbu):
    global verticies
    delta=sudut/100
    N=100
    while (N>0):
        nverticies=[]
        for vertex in verticies:
            vx=createpoint3D(vertex[0],vertex[1],vertex[2])
            v=Rotate3(list(vx),delta,P2,sumbu)
            x=v.tolist()
            nverticies.append(x)
        verticies=nverticies
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1


def operate(opr):
    print(opr)
    valid = False
    if (opr[0]=='translate'): #translasi
        if(len(opr) == 4):
            if (RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                dx = float(opr[1])
                dy = float(opr[2])
                dz = float(opr[3])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Translate3(list(vx),dx,dy,dz)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid = True


    elif (opr[0]=='dilate'): #dilasi
        if(len(opr) == 2):
            if(RepresentFloat(opr[1])):
                k = float(opr[1])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Dilate3(list(vx),k)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid = True


    elif (opr[0] =='rotate'): #rotasi
        if(len(opr) == 6):
            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4])):
                sumbu=opr[5]
                sudut= float(opr[1])
                P1 = (float(opr[2]), float(opr[3]), float(opr[4]))
                P2=createpoint3D(P1[0],P1[1],P1[2])
                
                animaterotate(sudut,P2,sumbu)
                valid = True

    elif(opr[0] =='reflect'): #refleksi
        if(len(opr) == 2):
            if(True):
                param=input('Masukkan parameter:\n')
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Reflect3(list(vx),param)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid = True

    elif(opr[0]=='shear'): #shear
        if(len(opr) == 4):
            if(RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                sumbu = opr[1]
                k1 = float(opr[2])
                k2 = float(opr[3])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Shear3(list(vx),sumbu,k1,k2)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid = True


    elif(opr[0]=='stretch'): #stretch
       if(len(opr)==3):
            if(RepresentFloat(opr[2])):
                sumbu=opr[1]
                k=float(opr[2])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Stretch2(list(vx),sumbu,k)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True


    elif(opr[0]=='custom'): #custom
        if(len(opr) == 10):
            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4]) and RepresentFloat(opr[5]) and RepresentFloat(opr[6]) and RepresentFloat(opr[7]) and RepresentFloat(opr[8]) and RepresentFloat(opr[9])):
                a=float(opr[1])
                b=float(opr[2])
                c=float(opr[3])
                d=float(opr[4])
                e=float(opr[5])
                f=float(opr[6])
                g=float(opr[7])
                h=float(opr[8])
                i=float(opr[9])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Custom3(list(vx),a,b,c,d,e,f,g,h,i)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid = True

    elif(opr[0]=='multi'): #multiple
        if(len(opr) == 2):
            if(RepresentFloat(opr[1])):
                n = opr[1]
                print('Multi ', n, ' kali START')
                nverticies=[]
                mverticies=verticies
                while (n>0):
                    print ('Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Multi\n')
                    oprx = input('Masukkan operan')
                    opr = [n for n in oprx.split(' ')]
                    if (opr[0]=='translate'): #translasi
                        if(len(opr) == 4):
                            if (RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                                dx = float(opr[1])
                                dy = float(opr[2])
                                dz = float(opr[3])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Translate3(list(vx),dx,dy,dz)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid = True

                            

                    elif (opr[0]=='dilate'): #dilasi
                        if(len(opr) == 2):
                            if(RepresentFloat(opr[1])):
                                k = float(opr[1])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Dilate3(list(vx),k)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid = True


                    elif (opr[0] =='rotate'): #rotasi
                        if(len(opr) == 6):
                            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4])):
                                sumbu=opr[5]
                                sudut= float(opr[1])
                                P1 = (float(opr[2]), float(opr[3]), float(opr[4]))
                                P2=createpoint3D(P1[0],P1[1],P1[2])
                                

                                animaterotate(sudut,P2,sumbu)
                                valid = True

                    elif(opr[0] =='reflect'): #refleksi
                        if(len(opr) == 2):
                            if(True):
                                param=input('Masukkan parameter:\n')
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Reflect3(list(vx),param)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid = True

                    elif(opr[0]=='shear'): #shear
                        if(len(opr) == 4):
                            if(RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                                sumbu = opr[1]
                                k1 = float(opr[2])
                                k2 = float(opr[3])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Shear3(list(vx),sumbu,k1,k2)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid = True


                    elif(opr[0]=='stretch'): #stretch
                        if(len(opr)==3):
                            if(RepresentFloat(opr[2])):
                                sumbu=opr[1]
                                k=float(opr[2])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Stretch2(list(vx),sumbu,k)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True


                    elif(opr[0]=='custom'): #custom
                        if(len(opr) == 10):
                            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4]) and RepresentFloat(opr[5]) and RepresentFloat(opr[6]) and RepresentFloat(opr[7]) and RepresentFloat(opr[8]) and RepresentFloat(opr[9])):
                                a=float(opr[1])
                                b=float(opr[2])
                                c=float(opr[3])
                                d=float(opr[4])
                                e=float(opr[5])
                                f=float(opr[6])
                                g=float(opr[7])
                                h=float(opr[8])
                                i=float(opr[9])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Custom3(list(vx),a,b,c,d,e,f,g,h,i)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid = True
                    if(valid == False):
                        print('Input salah')
                    n -= 1
                animate(mverticies)
                valid = True
    elif(opr[0] == 'reset'):
        nverticies = overticies
        animate(nverticies)
        valid = True
    if (valid == False):
        print('Input salah')

                    

def inputpoint3d():
    valid = False
    TruList=[]
    while(not(valid)) or (not(len(TruList) == 3)):
        TruList=[]
        instr = input('Enter a point (x,y,z): ')
        inList = [float(n) for n in instr.split(',')]
        for n in inList:
            valid = RepresentFloat(n)
            if (not(valid)):
                print('Input Salah!\n')
                break
            else:
                TruList.append(float(n))
        if (not(len(inList) == 3)) :
            print('Input harus (x,y,z)\n')
    TruList.append(0)
    return tuple(TruList)

def refresh():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cartesius()
    Cube()

    pygame.display.flip()
    clock.tick(60)

def main():
    pygame.init()

    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    
    Cartesius()
    setCube()

    pygame.display.set_caption('Algeo Yeah!!!')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    gluLookAt(3.0, 3.0, 5.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    op='Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n8.Multi \n9.Reset\n'
    print('Menunggu input dari window pygame...\n r=operasi\n  m/n=zoom in/zoom out\n')
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_r:
                operasi=input(op)
                operasi = [n for n in operasi.split(' ')]
                operate(operasi)
                print('Menunggu input dari window pygame...\n r=operasi\n  m/n=zoom in/zoom out\n')
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