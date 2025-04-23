import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.5, 2.5, 3.5, 4.5, 6.5, 9])

ln_y = np.log(y)

coeffs = np.polyfit(x, ln_y, 1)
b = coeffs[0]
ln_a = coeffs[1]
a = np.exp(ln_a)

def modelo_exponencial(x, a, b):
    return a * np.exp(b * x)

x_pred = np.linspace(min(x), max(x), 100)
y_pred = modelo_exponencial(x_pred, a, b)

print(f"Modelo ajustado: y = {a:.4f} * e^({b:.4f} * x)")

# Graficar
plt.scatter(x, y, label="Datos originales", color="blue")
plt.plot(x_pred, y_pred, label="Modelo exponencial ajustado", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regresión exponencial por mínimos cuadrados")
plt.legend()
plt.grid(True)
plt.show()
