from tools import *
from math import pi


def method_of_average_rectangles(a, b, n: int):
    integral = 0
    h = (b - a) / n
    for i in range(n):
        x = i*h + (h / 2)
        integral += f(x)
    return integral*h            
    


print(method_of_average_rectangles(0, pi / 2, 30))
