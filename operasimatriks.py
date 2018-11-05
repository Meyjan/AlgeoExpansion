import numpy as np

# Input point
def inputpoint():
    instr = input('Enter a point (x,y): ')
    point = np.array([float(n) for n in instr.split(',')])
    return point

# Translasi 2 dimensi
def Translate2(P, x, y):
    MTrans = np.array([x,y])
    P = np.add(MTrans, P)
    return (P)

# Rotasi 2 dimensi
def Rotate2(P, sudut):
    MTrans = np.array([[np.cos(np.deg2rad(sudut)), np.sin(np.deg2rad(sudut))], [np.sin(np.deg2rad((-1)*sudut)), np.cos(np.deg2rad(sudut))]])
    P = np.dot(MTrans, P)
    return (P)


# Tester
def main():
    # Cek input
    P1 = inputpoint()
    P2 = inputpoint()
    print("P1 = ", P1)
    print("P2 = ", P2)

    # Cek translasi
    x = float(input('Masukkan mau digeser ke sumbu x berapa jauh : '))
    y = float(input('Masukkan mau digeser ke sumbu y berapa jauh : '))
    P1 = Translate2(P1, x, y)
    print("P1 = ", P1)

    # Cek rotasi
    sudut = float(input('Masukkan sudut yang diputar : '))
    P1 = Rotate2(P1, sudut)
    print("P1 = ", P1)

main()
