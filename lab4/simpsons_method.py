from tools import *
from math import pi


def simpsons_method(a, b, n: int):
    integral = 0
    h = (b - a) / n
    fa = f(a)
    fb = f(b)
    for i in range(1, n+1):
        x = a + i*h
        if i % 2 == 0:
            integral += 2*f(x)
        else:
            integral += 4*f(x)
            
    
    return (h / 3) * (fa + fb + integral)


print(simpsons_method(0, pi / 2, 10))
