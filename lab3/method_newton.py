from tools import compute_jacobian, equations, calculate_inverse_matrix


def method_newton(x0: tuple, e: float, max_iteration: int = 100):
    x = list(x0)

    for iteration in range(max_iteration):
        jacobi = compute_jacobian(x)
        jacobi_inverted = calculate_inverse_matrix(jacobi)
        f_i = equations(x)

        xold = x.copy()
        for i in range(len(x)):
            x[i] = xold[i] - sum([to_sum[i] for to_sum in jacobi_inverted]) * f_i[i]

        if  all(abs(x[i] - xold[i]) / (abs(xold[i])) < e for i in range(len(xold))):
            print(iteration)
            return x


print("method_newton:",method_newton(x0=(0.1, 0.1), e=0.0001))
