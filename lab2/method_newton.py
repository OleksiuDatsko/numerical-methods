from tools import check, f, df, precision


def method_newton(x, e):
    count = 0
    xold = x
    x = x - f(x) / df(x)
    while precision(x, xold) > e:
        xold = x
        x = x - f(x) / df(x)
        count += 1
    print(count)
    return x, check(x, e)
