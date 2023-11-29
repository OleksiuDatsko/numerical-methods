import math
import matplotlib.pyplot as plt

# Відомі константи
U1 = lambda t: 100 * math.sin(2 * math.pi * 50 * t)
R1 = 5
R2 = 4
R4 = 2
L1 = 0.01
C1 = 300e-6

# Початкові умови
x0 = [0, 0]  # Початкові значення x[0] та x[1]

# Час для інтегрування
ti = 0.2
h = 0.00001
num_steps = int(ti / h)

# Зберігаємо результати в цих масивах
x0_values = []
x1_values = []
time_values = []

# Розраховуємо систему рівнянь методом Ейлера
for step in range(num_steps):
    t = step * h
    U1_t = U1(t)
    x0_dot = (U1_t - x0[0] + x0[1] * R2) / (C1 * (R1 + R2))
    x1_dot = (((U1_t - x0[0] - x0[1] * R1) / (R1 + R2)) * R2 - x0[1] * R4) / L1

    x0_new = x0[0] + h * x0_dot
    x1_new = x0[1] + h * x1_dot

    x0 = [x0_new, x1_new]

    x0_values.append(x0_new)
    x1_values.append(x1_new)
    time_values.append(t)

# Побудова графіка
plt.figure(figsize=(10, 6))
# plt.plot(time_values, x0_values, label='x[0]')
# plt.plot(time_values, x1_values, label='x[1]')
plt.plot(time_values, [x*R4 for x in x1_values], label='U2')
plt.plot(time_values, [U1(t) for t in time_values], label='U1')
plt.xlabel('Час')
plt.ylabel('Значення U1 та U2')
plt.legend()
plt.grid()
plt.title("Розв'язок системи рівнянь методом Ейлера")
plt.show()
