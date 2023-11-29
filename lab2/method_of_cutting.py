from tools import f, precision, check


def method_of_cutting(x0, x1, e):
    count = 0
    xold = x0
    x = x1
    xnew = None
    while precision(x, xold) > e:
        xnew = x - f(x) / ((f(xold) - f(x)) / (xold - x))
        xold = x
        x = xnew
        count += 1
    print(count)
    return xnew, check(xnew, e)
