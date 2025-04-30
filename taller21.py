import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([0, 2, 4, 6, 8, 10, 12])
y = np.array([7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2])

coeffs = np.polyfit(x, y, 2)
polinomio = np.poly1d(coeffs)

y_pred = polinomio(x)

r_squared = r2_score(y, y_pred)

correlation_matrix = np.corrcoef(y, y_pred)
correlation_coefficient = correlation_matrix[0, 1]

print(f"Polinomio ajustado: {polinomio}")
print(f"Coeficiente de determinación (R²): {r_squared:.4f}")
print(f"Coeficiente de correlación: {correlation_coefficient:.4f}")

x_line = np.linspace(min(x), max(x), 500)
y_line = polinomio(x_line)

plt.scatter(x, y, color='red', label='Datos')
plt.plot(x_line, y_line, color='blue', label='Ajuste polinomial')
plt.title('Ajuste de polinomio de segundo grado')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
