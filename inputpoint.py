import numpy as np

# Input point
def inputpoint(point):
    instr = input('Enter a point (x,y): ')
    inList = [float(n) for n in instr.split(',')]
    point = tuple(inList)
    print(point)
    print(point[0])
    print(point[1])

inputpoint()
