import numpy as np

# Represents float
def RepresentFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Create point
def createpoint2D(a, b):
    point = np.array([a, b])
    point = np.append(point, [0])
    return point
def createpoint3D(a, b, c):
    point = np.array([a, b, c])
    return point

# Input point
def inputpoint2D():
    instr = input('Enter a point (x,y): ')
    point = np.array([float(n) for n in instr.split(',')])
    point = np.append(point, [0])
    return point
def inputpoint3D():
    instr = input('Enter a point (x,y,z): ')
    point = np.array([float(n) for n in instr.split(',')])
    return point

# Translasi 2 dimensi
def Translate2(P, dx, dy):
    MTrans = np.array([dx,dy,0])
    P = np.add(MTrans, P)
    return(P)

# Translasi 3 dimenasi
def Translate3(P, dx, dy, dz):
    MTrans = np.array([dx,dy,dz])
    P = np.add(MTrans, P)
    return(P)

# Dilatasi 2 dimensi
def Dilate2(P, k):
    MTrans = np.array([[k, 0, 0], [0, k, 0], [0, 0, 1]])
    P = np.dot(MTrans, P)
    return(P)

# Dilatasi 3 dimensi
def Dilate3(P, k):
    MTrans = np.array([[k, 0, 0], [0, k, 0], [0, 0, k]])
    P = np.dot(MTrans, P)
    return(P)

# Rotasi 2 dimensi
def Rotate2(P, sudut, P2):
    MTrans = np.array([[np.cos(np.deg2rad(sudut)), np.sin(np.deg2rad((-1)*sudut)), 0], [np.sin(np.deg2rad(sudut)), np.cos(np.deg2rad(sudut)), 0], [0, 0, 1]])
    P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    P = np.round(P, 2)
    return(P)

# Rotasi 3 dimensi
def Rotate3(P, sudut, sumbu):
    P2 = np.array([0,0,0])
    a = np.cos(np.deg2rad(sudut))
    b = np.sin(np.deg2rad(sudut))
    # Rotasi terhadap sumbu
    if (sumbu == 'z') or (sumbu == 'Z'):
        MTrans = np.array([[a, b*(-1), 0], [b, a, 0], [0, 0, 1]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    elif (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[1, 0, 0], [0, a, b*(-1)], [0, b, a]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[a, 0, b], [0, 1, 0], [b*(-1), 0, a]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    # Rotasi terhadap garis
    # Sumbu dibuat dalam bentuk parametrik seperti (x,1,)
    else:
        print('Input tidak dikenal')

    P = np.round(P, 2)
    return (P)

# Refleksi 2 dimensi
def Reflect2(P, param):
    # Refleksi terhadap sumbu
    if (param == 'x') or (param == 'X'):
        MTrans = np.array([[1, 0, 0],[0, -1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y') or (param == 'Y'):
        MTrans = np.array([[-1, 0, 0],[0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    # Refleksi terhadap garis
    elif (param == 'y=x') or (param == 'Y=X'):
        MTrans = np.array([[0, 1, 0],[1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=-x') or (param == 'Y=-X'):
        MTrans = np.array([[0, -1, 0],[-1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    # Refleksi terhadap titik
    else:
        param = param[1:-1]
        point = np.array([float(n) for n in param.split(',')])
        point = np.append(point, [0])
        P = np.subtract(np.dot(point, 2), P)
        return(P)

# Refleksi 3 dimenasi
def Reflect3(P, param):
    # Refleksi terhadap bidang
    if (param == 'xz') or (param == 'XZ'):
        MTrans = np.array([[1, 0, 0],[0, -1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'yz') or (param == 'YZ'):
        MTrans = np.array([[-1, 0, 0],[0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'xy') or (param == 'XY'):
        MTrans = np.array([[1, 0, 0],[0, 1, 0], [0, 0, -1]])
        P = np.dot(MTrans, P)
        return(P)
    # Refleksi terhadap sumbu
    elif (param == 'x') or (param == 'X'):
        MTrans = np.array([[1, 0, 0],[0, -1, 0], [0, 0, -1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y') or (param == 'Y'):
        MTrans = np.array([[-1, 0, 0],[0, 1, 0], [0, 0, -1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'z') or (param == 'Z'):
        MTrans = np.array([[-1, 0, 0],[0, -1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    # Refleksi terhadap bidang lain
    elif (param == 'y=x') or (param == 'Y=X'):
        MTrans = np.array([[0, 1, 0],[1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=-x') or (param == 'Y=-X'):
        MTrans = np.array([[0, -1, 0],[-1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=z') or (param == 'Y=Z'):
        MTrans = np.array([[1, 0, 0],[0, 0, 1], [0, 1, 0]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=-z') or (param == 'Y=-Z'):
        MTrans = np.array([[1, 0, 0],[0, 0, -1], [0, -1, 0]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'x=z') or (param == 'X=Z'):
        MTrans = np.array([[0, 0, 1],[0, 1, 0], [1, 0, 0]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'x=-z') or (param == 'X=-Z'):
        MTrans = np.array([[0, 0, -1],[0, 1, 0], [-1, 0, 0]])
        P = np.dot(MTrans, P)
        return(P)
    # Refleksi terhadap garis
    elif (param == 'x=y=z') or (param == 'X=Y=Z'):
        x = (P[0]+P[1]+P[2])/3
        print (x)
        P2 = np.array([(x-P[0]), (x-P[1]), (x-P[2])])
        print (P2)
        P = np.add(P, np.dot(P2, 2))
        return (P)
    elif (param == 'x=y=-z') or (param == 'X=Y=-Z'):
        x = (P[0]+P[1]-P[2])/3
        P2 = np.array([(x-P[0]), (x-P[1]), (-x-P[2])])
        P = np.add(P, np.dot(P2, 2))
        return (P)
    elif (param == 'x=-y=z') or (param == 'X=-Y=Z'):
        x = (P[0]-P[1]+P[2])/3
        P2 = np.array([(x-P[0]), (-x-P[1]), (x-P[2])])
        P = np.add(P, np.dot(P2, 2))
        return (P)
    elif (param == '-x=y=z') or (param == '-X=Y=Z'):
        x = (-P[0]+P[1]+P[2])/3
        P2 = np.array([(-x-P[0]), (x-P[1]), (x-P[2])])
        P = np.add(P, np.dot(P2, 2))
        return (P)
    # Refleksi terhadap titik
    else:
        param = param[1:-1]
        point = np.array([float(n) for n in param.split(',')])
        P = np.subtract(np.dot(point, 2), P)
        return(P)

# Shear 2 dimensi
def Shear2(P, sumbu, k):
    if (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[1, k, 0], [0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[1, 0, 0], [k, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    else:
        print('Input tidak diterima')
        return (P)

# Shear 3 dimenasi
def Shear3(P, sumbu, k1, k2):
    if (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[1, k1, k2], [0, 1, 0],[0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[1, 0, 0], [k1, 1, k2], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'z') or (sumbu == 'Z'):
        MTrans = np.array([[1, 0, 0], [0, 1, 0], [k1, k2, 1]])
        P = np.dot(MTrans, P)
        return (P)
    else:
        print('Input tidak diterima')
        return (P)

# Stretch 2 dimensi
def Stretch2(P, sumbu, k):
    if (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[k, 0, 0], [0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[1, 0, 0], [0, k, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    else:
        print('Input tidak diterima')
        return (P)

# Stretch 3 dimensi
def Stretch3(P, sumbu, k):
    if (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[k, 0, 0], [0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[1, 0, 0], [0, k, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return (P)
    elif (sumbu == 'z') or (sumbu == 'Z'):
        MTrans = np.array([[1, 0, 0], [0, 1, 0], [0, 0, k]])
        P = np.dot(MTrans, P)
        return (P)
    else:
        print('Input tidak diterima')
        return (P)

# Custom 2 dimensi
def Custom2(P, a, b, c, d):
    MTrans = np.array([[a, b, 0], [c, d, 0], [0, 0, 1]])
    P = np.dot(MTrans, P)
    return (P)

# Custom 3 dimensi
def Custom3(P, a, b, c, d, e, f, g, h, i):
    MTrans = np.array([[a, b, c], [d, e, f], [g, h, i]])
    P = np.dot(MTrans, P)
    return (P)


# Multiple 2 dimensi
# Gunakan matriks transformasi di atas untuk melakukan perkalian selama input masuk 1 per 1
# Lalu tinggal tunjukkan hasil nantinya
# Kaya masukkan input biasa tapi sampai beres multinya jangan ditampilin dulu

# Multiple 3 dimensi
# Gunakan matriks transformasi di atas untuk melakukan perkalian selama input masuk 1 per 1
# Lalu tinggal tunjukkan hasil nantinya
# Kaya masukkan input biasa tapi sampai beres multinya jangan ditampilin dulu

# Reset
# Copy titik-titik di program utama agar tinggal dipanggil lagi nanti

# Tester
def main():
    # Cek input
    i = int(input('2D or 3D? {2/3}: '))
    while ((i != 2) and (i != 3)):
        print ('Wrong input!')
        i = int(input('2D or 3D? {2/3}: '))

    # Input point
    if (i == 2):
        P1 = inputpoint2D()
    elif (i == 3):
        P1 = inputpoint3D()
    P2 = P1
    print('P1 = ', P1)
    print('P2 = ', P2)

    # Tester
    c = input('Masukkan input perintah : ')

    while (c != 'STOP'):
        # Cek translasi 2 dimensi
        if (c == 'Translate2'):
            x = float(input('Masukkan mau digeser ke sumbu x berapa jauh : '))
            y = float(input('Masukkan mau digeser ke sumbu y berapa jauh : '))
            P1 = Translate2(P1, x, y)
            print('Translate2 P1 = ', P1)
        # Cek translasi 3 dimensi
        elif (c == 'Translate3'):
            x = float(input('Masukkan mau digeser ke sumbu x berapa jauh : '))
            y = float(input('Masukkan mau digeser ke sumbu y berapa jauh : '))
            z = float(input('Masukkan mau digeser ke sumbu z berapa jauh : '))
            P1 = Translate3(P1, x, y, z)
            print('Translate3 P1 = ', P1)

        # Cek dilatasi 2 dimensi
        elif (c == 'Dilate2'):
            k = float(input('Mau didilatasi seberapa jauh? -> '))
            P1 = Dilate2(P1, k)
            print('Dilate2 P1 = ', P1)
        # Cek dilatasi 3 dimensi
        elif (c == 'Dilate3'):
            k = float(input('Mau didilatasi seberapa jauh? -> '))
            P1 = Dilate3(P1, k)
            print('Dilate3 P1 = ', P1)

        # Cek rotasi 2 dimensi
        elif (c == 'Rotate2'):
            sudut = float(input('Masukkan sudut yang diputar : '))
            print('Masukkan titik poros yang mau diputar!')
            P3 = inputpoint2D()
            P1 = Rotate2(P1, sudut, P3)
            print('Rotate2 P1 = ', P1)
        # Cek rotasi 3 dimensi
        elif (c == 'Rotate3'):
            sudut = float(input('Masukkan sudut yang diputar : '))
            sumbu = input('Masukkan mau terhadap sumbu mana diputar : ')
            P1 = Rotate3(P1, sudut, sumbu)
            print('Rotate3 P1 = ', P1)

        # Cek refleksi 2 dimensi
        elif (c == 'Reflect2'):
            param = input('Masukkan parameter dari refleksi : ')
            P1 = Reflect2 (P1, param)
            print('Reflect2 P1 = ', P1)
        # Cek refleksi 3 dimensi
        elif (c == 'Reflect3'):
            param = input('Masukkan parameter dari refleksi : ')
            P1 = Reflect3 (P1, param)
            print('Reflect3 P1 = ', P1)

        # Cek shear 2 dimensi
        elif (c == 'Shear2'):
            sumbu = input('Masukkan sumbu untuk shear : ')
            k = float(input('Masukkan konstanta untuk shear : '))
            P1 = Shear2 (P1, sumbu, k)
            print('Shear2 P1 = ', P1)
        # Cek shear 3 dimensi
        elif (c == 'Shear3'):
            sumbu = input('Masukkan sumbu untuk shear : ')
            k1 = float(input('Masukkan konstanta 1 untuk shear : '))
            k2 = float(input('Masukkan konstanta 2 untuk shear : '))
            P1 = Shear3 (P1, sumbu, k1, k2)
            print('Shear3 P1 = ', P1)

        # Cek stretch 2 dimensi
        elif (c == 'Stretch2'):
            sumbu = input('Masukkan sumbu untuk stretch : ')
            k = float(input('Masukkan konstanta untuk stretch : '))
            P1 = Stretch2 (P1, sumbu, k)
            print('Stretch2 P1 = ', P1)
        # Cek stretch 3 dimensi
        elif (c == 'Stretch3'):
            sumbu = input('Masukkan sumbu untuk stretch : ')
            k = float(input('Masukkan konstanta untuk stretch : '))
            P1 = Stretch3 (P1, sumbu, k)
            print('Stretch3 P1 = ', P1)

        # Cek custom 2 dimensi
        elif (c == 'Custom2'):
            a = float(input('Masukkan konstanta matriks a : '))
            b = float(input('Masukkan konstanta matriks b : '))
            c = float(input('Masukkan konstanta matriks c : '))
            d = float(input('Masukkan konstanta matriks d : '))
            P1 = Custom2(P1, a, b, c, d)
            print('Custom2 P1 = ', P1)
        # Cek custom 3 dimensi
        elif (c == 'Custom3'):
            a = float(input('Masukkan konstanta matriks a : '))
            b = float(input('Masukkan konstanta matriks b : '))
            c = float(input('Masukkan konstanta matriks c : '))
            d = float(input('Masukkan konstanta matriks d : '))
            e = float(input('Masukkan konstanta matriks e : '))
            f = float(input('Masukkan konstanta matriks f : '))
            g = float(input('Masukkan konstanta matriks g : '))
            h = float(input('Masukkan konstanta matriks h : '))
            i = float(input('Masukkan konstanta matriks i : '))
            P1 = Custom3(P1, a, b, c, d, e, f, g, h, i)
            print('Custom3 P1 = ', P1)

        # Cek reset
        elif (c == 'Reset'):
            P1 = P2
            print('Reset P1 = ', P1)
        # Lain-lain
        else:
            print('Input tidak dikenal')

        # Input lagi
        c = input('Masukkan input perintah : ')

    print('Program done. Terminating...')

main()
