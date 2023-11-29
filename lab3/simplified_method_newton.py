from tools import compute_jacobian, equations, calculate_inverse_matrix

def simplified_method_newton(x0: tuple, e: float, max_iteration: int = 100):
    x = list(x0)
    jacobi = compute_jacobian(x)
    jacobi_inverted = calculate_inverse_matrix(jacobi)
    for iteration in range(max_iteration):
        f_i = equations(x)

        xold = x.copy()
        for i in range(len(x)):
            x[i] = xold[i] - sum([to_sum[i] for to_sum in jacobi_inverted])*f_i[i]
        
        
        if all(abs(x[i] - xold[i]) / (abs(xold[i])) < e for i in range(len(xold))):
            print(iteration)
            return x
    return None
    
print("simplified_method_newton:",simplified_method_newton(x0=(1, 1), e=0.01))