from tools import *
from math import pi


def trapezium_method(a, b, n: int):
    integral = 0
    h = (b - a) / n
    x = a + h
    fa = f(a)
    fb = f(b)
    for i in range(1, n - 1):
        integral += f(x)
        x = x + h

    return h * (((fa + fb) / 2) + integral)


print(trapezium_method(0, pi / 2, 30))

# порахувати похибку для  300 точок -> порівняти з 30
