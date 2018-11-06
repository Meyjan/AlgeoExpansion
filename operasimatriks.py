import numpy as np

#Ferdy tae

# Represents float
def RepresentFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Input point
def inputpoint():
    instr = input('Enter a point (x,y,z): ')
    point = np.array([float(n) for n in instr.split(',')])
    return point

# Translasi 2 dimensi
def Translate2(P, dx, dy):
    MTrans = np.array([dx,dy,0])
    P = np.add(MTrans, P)
    return(P)

# Dilatasi 2 dimensi
def Dilate2(P, k):
    MTrans = np.array([[k, 0, 0], [0, k, 0], [0, 0, k]])
    P = np.dot(MTrans, P)
    return(P)

# Rotasi 2 dimensi
def Rotate2(P, sudut, P2):
    MTrans = np.array([[np.cos(np.deg2rad(sudut)), np.sin(np.deg2rad((-1)*sudut)), 0], [np.sin(np.deg2rad(sudut)), np.cos(np.deg2rad(sudut)), 0], [0, 0, 1]])
    P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    return(P)

# Refleksi 2 dimensi
def Reflect2(P, param):
    if (param == 'x') or (param == 'X'):
        MTrans = np.array([[1,0],[0,-1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y') or (param == 'Y'):
        MTrans = np.array([[-1,0],[0,1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=x') or (param == 'Y=X'):
        MTrans = np.array([[0,1],[1,0]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=-x') or (param == 'Y=-X'):
        MTrans = np.array([[0,-1],[-1,0]])
        P = np.dot(MTrans, P)
        return(P)
    else:
        point = np.array([float(n) for n in instr.split(',')])


# Lain-lain

# Custom 2 dimensi

# Tester
def main():
    # Cek input
    P1 = inputpoint()
    P2 = P1
    print('P1 = ', P1)
    print('P2 = ', P2)

    # Cek translasi
    x = float(input('Masukkan mau digeser ke sumbu x berapa jauh : '))
    y = float(input('Masukkan mau digeser ke sumbu y berapa jauh : '))
    P1 = Translate2(P1, x, y)
    print('P1 = ', P1)

    # Cek dilatasi
    k = float(input('Mau didilatasi seberapa jauh?'))
    P1 = Dilate2(P1, k)
    print('P1 = ', P1)

    # Cek rotasi
    sudut = float(input('Masukkan sudut yang diputar : '))
    print('Masukkan titik yang mau diputar!', end = '')
    P3 = inputpoint()
    P1 = Rotate2(P1, sudut, P3)
    print('P1 = ', P1)

    # Reset
    P1 = P2
    print('P1 = ', P1)

main()
