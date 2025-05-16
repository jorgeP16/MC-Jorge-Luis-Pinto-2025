import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 5, 2.5, 4, -1.6, 2])
x_val = 3.55

lagrange_poly = lagrange(x, y)
lagrange_est = lagrange_poly(x_val)

cubic_spline = CubicSpline(x, y)
cubic_est = cubic_spline(x_val)

x_dense = np.linspace(min(x), max(x), 400)
y_lagrange = lagrange_poly(x_dense)
y_cubic = cubic_spline(x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Datos originales')
plt.plot(x_dense, y_lagrange, label='Interpolación de Lagrange', linestyle='--')
plt.plot(x_dense, y_cubic, label='Trazadores Cúbicos', linestyle='-')
plt.scatter([x_val], [lagrange_est], color='red', label=f'Lagrange f({x_val:.2f}) ≈ {lagrange_est:.2f}')
plt.scatter([x_val], [cubic_est], color='green', label=f'Cúbicos f({x_val:.2f}) ≈ {cubic_est:.2f}')
plt.title('Interpolación: Lagrange vs Trazadores Cúbicos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Valor estimado por Lagrange en x = {x_val}: {lagrange_est}")
print(f"Valor estimado por Trazadores Cúbicos en x = {x_val}: {cubic_est}")
