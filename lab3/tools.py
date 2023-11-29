import numpy as np


def f1(x):
    return (x[0] ** 2) - (x[1] ** 2) + 0.1 - x[0]


def df1_dx1(x):
    return 2 * x[0] - 1


def df1_dx2(x):
    return -2 * x[1]


def f2(x):
    return (2 * x[0] * x[1]) + 0.1 - x[1]


def df2_dx1(x):
    return 2 * x[1]


def df2_dx2(x):
    return 2 * x[0] + 1


def equations(x: list):
    result = [f1(x), f2(x)]
    return result


def compute_jacobian(x: list):
    result = [[df1_dx1(x), df1_dx2(x)], 
              [df2_dx1(x), df2_dx2(x)]]
    return result


def calculate_inverse_matrix(A):
    A = np.array(A)
    n = A.shape[0]
    m = np.hstack((A, np.eye(n)))

    for nrow, row in enumerate(m):
        divider = row[nrow]
        row /= divider
        for lower_row in m[nrow + 1 :]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    for k in range(n - 1, 0, -1):
        for row_ in range(k - 1, -1, -1):
            if m[row_, k]:
                m[row_, :] -= m[k, :] * m[row_, k]

    return m[:, n:].tolist()
