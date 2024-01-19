from tools import check, f, df, precision

def method_newton(x, e):
    xold = x
    x = x - f(x) / df(x)
    while precision(x, xold) > e:
        xold = x
        x = x - f(x) / df(x)
    return x, check(x, e)
