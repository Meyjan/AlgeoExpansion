import numpy as np

from operasimatriks import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

objects=[]

class obj:
    def __init__(self,verticies,overticies,edges,shape,color):
        self.v=verticies
        self.o=overticies
        self.e=edges
        self.s=shape
        self.c=color

idx=0

color=0

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
    global color
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
    ob=obj(verticies,overticies,edges,shape,color)
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
    global color
    x=input('Masukkan warna: \n 1. Merah\n 2. Hijau\n 3. Biru\n 4. Cyan\n 5. Kuning\n 6. Magenta\n 7. Putih \n 8. Hitam\n')
    while(x<'1' or x>'8'):
        x=input('Salah input\n')
    color=int(x)-1
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
    for vertex in verticies:
        glColor3fv(colors[color])
        glVertex3fv(vertex)
    glEnd()

def setPolygon():
    global verticies
    global color
    x=input('Masukkan warna: \n 1. Merah\n 2. Hijau\n 3. Biru\n 4. Cyan\n 5. Kuning\n 6. Magenta\n 7. Putih \n 8. Hitam\n')
    while(x<'1' or x>'8'):
        x=input('Salah input\n')
    color=int(x)-1
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
    for vertex in verticies:
        glColor3fv(colors[color])
        glVertex3fv(vertex)
    glEnd()

def setCircle():
    global verticies
    global color
    x=input('Masukkan warna: \n 1. Merah\n 2. Hijau\n 3. Biru\n 4. Cyan\n 5. Kuning\n 6. Magenta\n 7. Putih \n 8. Hitam\n')
    while(x<'1' or x>'8'):
        x=input('Salah input\n')
    color=int(x)-1
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
    for vertex in verticies:
        glColor3fv(colors[color])
        glVertex3fv(vertex)
    glEnd()

def setTriangle():
    global verticies
    global color
    x=input('Masukkan warna: \n 1. Merah\n 2. Hijau\n 3. Biru\n 4. Cyan\n 5. Kuning\n 6. Magenta\n 7. Putih \n 8. Hitam\n')
    while(x<'1' or x>'8'):
        x=input('Salah input\n')
    color=int(x)-1
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
    for vertex in verticies:
        glColor3fv(colors[color])
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
    return tuple(TruList)

def refresh():
    global verticies
    global edges
    global shape
    global color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for ob in objects:
        verticies=ob.v
        edges=ob.e
        shape=ob.s
        color=ob.c
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
    verticies=objects[idx].v
    edges=objects[idx].e
    shape=objects[idx].s
    color=objects[idx].c
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
        verticies=nverticies
        objects[idx].v=verticies
        refresh()
        gamecontrol()
        pygame.time.wait(50)
        N-=1

def operate(opr):
    valid=False
    if (opr[0]=='translate'):
        if (len(opr)==3):
            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2])):
                dx=float(opr[1])
                dy=float(opr[2])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Translate2(list(vx),dx,dy)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True
    elif (opr[0]=='dilate'):
        if(len(opr)==2):
            if(RepresentFloat(opr[1])):
                k=float(opr[1])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Dilate2(list(vx),k)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True
    elif (opr[0]=='rotate'):
        if(len(opr)==4):
            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                sudut=float(opr[1])
                P1=(float(opr[2]),float(opr[3]),0)
                P2=createpoint3D(P1[0],P1[1],P1[2])
                animaterotate(sudut,P2)
                valid=True
    elif(opr[0]=='reflect'):
        if(len(opr)==2):
            if(True):
                param=input('Masukkan parameter:\n')
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Reflect2(list(vx),param)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True
    elif(opr[0]=='shear'):
        if(len(opr)==3):
            if(RepresentFloat(opr[2])):
                sumbu=opr[1]
                k=float(opr[2])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Shear2(list(vx),sumbu,k)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True
    elif(opr[0]=='stretch'):
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
    elif(opr[0]=='custom'):
        if(len(opr)==5):
            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4])):
                a=float(opr[1])
                b=float(opr[2])
                c=float(opr[3])
                d=float(opr[4])
                nverticies=[]
                for vertex in verticies:
                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                    v=Custom2(list(vx),a,b,c,d)
                    x=v.tolist()
                    nverticies.append(x)
                animate(nverticies)
                valid=True
    elif(opr[0]=='multi'):
        if(len(opr)==2):
            if(RepresentFloat(opr[1])):
                n = opr[1]
                print('Multi ', n, ' kali START')
                nverticies=[]
                mverticies=verticies
                while (n>0):
                    print ('Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n')
                    opsx = input('Masukkan operan')
                    opr =[n for n in opsx.split(' ')]
                    if (opr[0]=='translate'):
                        if (len(opr)==3):
                            if(RepresentFloat(opr[1]) and RepresentFloat(2)):
                                dx=float(opr[1])
                                dy=float(opr[2])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Translate2(list(vx),dx,dy)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True
                    elif (opr[0]=='dilate'):
                        if(len(opr)==2):
                            if(RepresentFloat(opr[1])):
                                k=float(opr[1])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Dilate2(list(vx),k)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True
                    elif (opr[0]=='rotate'):
                        if(len(opr)==4):
                            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3])):
                                sudut=float(opr[1])
                                P1=(float(opr[2]),float(opr[3]),0)
                                P2=createpoint3D(P1[0],P1[1],P1[2])
                                animaterotate(sudut,P2)
                                valid=True
                    elif(opr[0]=='reflect'):
                        if(len(opr)==2):
                            if(True):
                                param=input('Masukkan parameter:\n')
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Reflect2(list(vx),param)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True
                    elif(opr[0]=='shear'):
                        if(len(opr)==3):
                            if(RepresentFloat(opr[2])):
                                sumbu=opr[1]
                                k=float(opr[2])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Shear2(list(vx),sumbu,k)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True
                    elif(opr[0]=='stretch'):
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
                    elif(opr[0]=='custom'):
                        if(len(opr)==5):
                            if(RepresentFloat(opr[1]) and RepresentFloat(opr[2]) and RepresentFloat(opr[3]) and RepresentFloat(opr[4])):
                                a=float(opr[1])
                                b=float(opr[2])
                                c=float(opr[3])
                                d=float(opr[4])
                                nverticies=[]
                                for vertex in verticies:
                                    vx=createpoint3D(vertex[0],vertex[1],vertex[2])
                                    v=Custom2(list(vx),a,b,c,d)
                                    x=v.tolist()
                                    nverticies.append(x)
                                animate(nverticies)
                                valid=True
                    if(valid==False):
                        print('Input salah')
                    n -= 1
                animate(mverticies)
                valid=True
    elif(opr[0]=='reset'):
        nverticies=overticies
        animate(nverticies)
        valid=True
    if(valid==False):
        print('Input salah')

def main():
    pygame.init()

    global objects
    global verticies
    global edges
    global shape
    global idx
    global color

    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    addobject()
    Cartesius()

    pygame.display.set_caption('Algeo Tubes Edition')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    op='Masukkan operasi:\n1. Translasi\n2. Dilatasi\n3. Rotasi\n4. Refleksi\n5. Shear\n6. Stretch\n7. Custom\n8. Multi\n9. Reset\n'
    print('Menunggu input dari window pygame...\n r=operasi\n c=cycle\n a=addobject\n m/n=zoom in/zoom out\n')
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_r:
                opxs=input(op)
                opxs=[n for n in opxs.split(' ')]
                operate(opxs)
                print('Menunggu input dari window pygame...\n r=operasi\n c=cycle\n a=addobject\n')
            if event.type == KEYDOWN and event.key == K_a:
                addobject()
                print('Menunggu input dari window pygame...\n r=operasi\n c=cycle\n a=addobject\n')
            if event.type == KEYDOWN and event.key == K_c:
                idx+=1
                idx=idx%len(objects)
                color=objects[idx].c
                verticies=objects[idx].v
                edges=objects[idx].e
                shape=objects[idx].s
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
