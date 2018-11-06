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

# Translasi 3 dimenasi
def Translate2(P, dx, dy, dz):
    MTrans = np.array([dx,dy,dz])
    P = np.add(MTrans, P)
    return(P)

# Dilatasi 2 dimensi
def Dilate2(P, k):
    MTrans = np.array([[k, 0, 0], [0, k, 0], [0, 0, 1]])
    P = np.dot(MTrans, P)
    return(P)

# Dilatasi 3 dimensi
def Dilate2(P, k):
    MTrans = np.array([[k, 0, 0], [0, k, 0], [0, 0, k]])
    P = np.dot(MTrans, P)
    return(P)

# Rotasi 2 dimensi
def Rotate2(P, sudut, P2):
    MTrans = np.array([[np.cos(np.deg2rad(sudut)), np.sin(np.deg2rad((-1)*sudut)), 0], [np.sin(np.deg2rad(sudut)), np.cos(np.deg2rad(sudut)), 0], [0, 0, 1]])
    P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
    return(P)

# Rotasi 3 dimensi
def Rotate3(P, sudut, P2, sumbu):
    a = np.cos(np.deg2rad(sudut))
    b = np.sin(np.deg2rad(sudut))
    if (sumbu == 'z') or (sumbu == 'Z'):
        MTrans = np.array([[a, b*(-1), 0], [b, a, 0], [0, 0, 1]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
        return(P)
    elif (sumbu == 'x') or (sumbu == 'X'):
        MTrans = np.array([[1, 0, 0], [0, a, b*(-1)], [0, b, a]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
        return(P)
    elif (sumbu == 'y') or (sumbu == 'Y'):
        MTrans = np.array([[b, 0, a], [0, 1, 0], [b*(-1), a]])
        P = np.add((np.dot(MTrans, np.subtract(P,P2))), P2)
        return(P)
    else:
        print ("Input tidak valid")
        return(P)

# Refleksi 2 dimensi
def Reflect2(P, param):
    if (param == 'x') or (param == 'X'):
        MTrans = np.array([[1, 0, 0],[0, -1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y') or (param == 'Y'):
        MTrans = np.array([[-1, 0, 0],[0, 1, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=x') or (param == 'Y=X'):
        MTrans = np.array([[0, 1, 0],[1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    elif (param == 'y=-x') or (param == 'Y=-X'):
        MTrans = np.array([[0, -1, 0],[-1, 0, 0], [0, 0, 1]])
        P = np.dot(MTrans, P)
        return(P)
    else:
        param = param[1:-1]
        point = np.array([float(n) for n in param.split(',')])
        point = np.append(point, [0])
        P = np.substract(np.dot(param, 2), P)
        return(P)

# Refleksi 3 dimenasi
# Belum

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
# Belum

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

# Belum

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
    print('Reset P1 = ', P1)

main()
