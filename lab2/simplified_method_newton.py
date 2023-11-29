from tools import check, f, df, precision


def simplified_method_newton(x, e):
    count = 0
    f_dx = df(x)

    xold = x
    x = x - f(x) / f_dx
    while precision(x, xold) > e:
        count += 1
        xold = x
        x = x - f(x) / f_dx
    print(count)
    return x, check(x, e)
