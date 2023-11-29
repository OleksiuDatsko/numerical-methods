from tools import *


def method_of_cutting(x0: tuple, e: float, max_iteration: int = 100):
    x = xold = list(x0)

    for iteration in range(max_iteration):
        f_i = equations(x)
        j = compute_jacobian(x)
        j_inverted = calculate_inverse_matrix(j)
        xold = x.copy()
        for i in range(len(x)):
            x[i] = xold[i] - sum([to_sum[i] for to_sum in j_inverted]) * f_i[i]

        if all(abs(x[i] - xold[i]) / (abs(xold[i])) < e for i in range(len(xold))):
            print(iteration)
            return x


print("method_of_cutting:",method_of_cutting(x0=(1, 1), e=0.01))
