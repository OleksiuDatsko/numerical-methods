import math

def f(x):
    return (x**3) + (x**2) - 3

def df(x):
    return (2*x) + (3*(x**2))

def precision(x, xold):
    return abs((x - xold) / x) * 100

def check(x, e):
    e = e / 100
    result = round(f(x), abs(int(math.log10(e))))
    return result <= (0.0 + e) and result >= (0.0 - e) 