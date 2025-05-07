import numpy as np
import matplotlib.pyplot as plt

x_base = np.array([1, 3, 5, 7, 9])
f_base = np.array([3, 0, -1, 2.5, 1])

x_estimar = 4.25

def lagrange_interpol(x, y, x_eval):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_eval - x[j]) / (x[i] - x[j])
        result += term
    return result

x1 = np.array([3, 5])
y1 = np.array([0, -1])

x2 = np.array([3, 5, 7])
y2 = np.array([0, -1, 2.5])

x3 = np.array([1, 3, 5, 7])
y3 = np.array([3, 0, -1, 2.5])

x_vals = np.linspace(1, 9, 200)

y_g1 = [lagrange_interpol(x1, y1, xi) for xi in x_vals]
y_g2 = [lagrange_interpol(x2, y2, xi) for xi in x_vals]
y_g3 = [lagrange_interpol(x3, y3, xi) for xi in x_vals]

res_g1 = lagrange_interpol(x1, y1, x_estimar)
res_g2 = lagrange_interpol(x2, y2, x_estimar)
res_g3 = lagrange_interpol(x3, y3, x_estimar)

print(f"Estimación f(4.25) grado 1: {res_g1:.4f}")
print(f"Estimación f(4.25) grado 2: {res_g2:.4f}")
print(f"Estimación f(4.25) grado 3: {res_g3:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_g1, label='Grado 1 (lineal)', linestyle='--')
plt.plot(x_vals, y_g2, label='Grado 2 (cuadrático)', linestyle='-.')
plt.plot(x_vals, y_g3, label='Grado 3 (cúbico)', linestyle=':')
plt.scatter(x_base, f_base, color='black', label='Puntos base')
plt.scatter(x_estimar, res_g1, color='blue', marker='o', label=f'Estimación G1: {res_g1:.2f}')
plt.scatter(x_estimar, res_g2, color='green', marker='s', label=f'Estimación G2: {res_g2:.2f}')
plt.scatter(x_estimar, res_g3, color='red', marker='^', label=f'Estimación G3: {res_g3:.2f}')

plt.title('Interpolación de Lagrange para f(4.25)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
