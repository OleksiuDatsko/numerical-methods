import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve

# Відомі константи
U1 = lambda t: 100 * math.sin(2 * math.pi * 50 * t)
R1 = 5
R2 = 4
R4 = 2
L1 = 0.01
C1 = 300e-6


def implicit_euler_method_system(f, x0, t0, tn, h):
    num_steps = int((tn - t0) / h)
    t_values = np.linspace(t0, tn, num_steps + 1)
    x_values = np.zeros((len(t_values), len(x0)))
    x_values[0] = x0

    for i in range(num_steps):
        x_prev = x_values[i]
        t = t_values[i]

        # Функція для розв'язання системи нелінійних рівнянь методом fsolve
        def equation(x_next):
            return x_prev + h * f(x_next, t + h) - x_next

        x_next_guess = x_prev + h * f(x_prev, t)  # Початкове наближення для x_next
        x_next_solution = fsolve(equation, x_next_guess)
        x_values[i + 1] = x_next_solution

    return t_values, x_values


# Приклад використання:
def f(x, t):
    # Приклад системи диференціальних рівнянь:
    dxdt = (U1(t) - x[0] + x[1] * R2) / (C1 * (R1 + R2))

    dydt = (((U1(t) - x[0] - x[1] * R1) / (R1 + R2)) * R2 - x[1] * R4) / L1
    return np.array([dxdt, dydt])


t0 = 0
tn = 0.2
x0 = np.array([0, 0])  # Початковий вектор x
h = 10 ** (-5)

time_values, x_values = implicit_euler_method_system(f, x0, t0, tn, h)


# Побудова графіка
plt.figure(figsize=(10, 6))
# plt.plot(time_values, x0_values, label='x[0]')
# plt.plot(time_values, x1_values, label='x[1]')
plt.plot(time_values, [x * R4 for x in x_values[:, 1]], label="U2")
plt.plot(time_values, [U1(t) for t in time_values], label="U1")
plt.xlabel("Час")
plt.ylabel("Значення U1 та U2")
plt.legend()
plt.grid()
plt.title("Розв'язок системи рівнянь неявний методом Ейлера")
plt.show()
