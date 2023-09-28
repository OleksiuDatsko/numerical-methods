from tools import check, f, df, precision

def simplified_method_newton(x, e):
    f_dx = df(x)

    xold = x
    x = x - f(x) / f_dx
    while precision(x, xold) > e:
        xold = x
        x = x - f(x) / f_dx
    return x, check(x, e)
   