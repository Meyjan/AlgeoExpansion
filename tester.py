import numpy as np
import re

# Tester

def RepresentFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


text = '(1,2)'
text = text[1:-1]
print(text)
point = np.array([float(n) for n in text.split(',')])
print(point)
point = np.append(point, [0])
print(point)
point = np.dot(point, 2)
print(point)
