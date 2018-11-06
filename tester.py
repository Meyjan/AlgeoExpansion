import numpy as np

# Tester

def RepresentFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


string = input('Input string : ')
point = np.array([float(n) for n in string.split(',')])
