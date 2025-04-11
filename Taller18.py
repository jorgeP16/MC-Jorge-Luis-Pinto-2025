import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos proporcionados
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0.5, 2, 3.5, 4.5, 9, 13.5])

# Cálculo de la regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Coeficiente de correlación (r)
r = r_value
# Coeficiente de determinación (r²)
r_squared = r_value**2

# Predicciones del modelo
y_pred = intercept + slope * x

# Cálculo de la desviación estándar de y (sy)
sy = np.std(y, ddof=1)

# Cálculo del error estándar de la estimación (sy/x)
# Fórmula: sqrt(sum((y - y_pred)²) / (n - 2))
n = len(x)
residuos = y - y_pred
sy_x = np.sqrt(np.sum(residuos**2) / (n - 2))

# Visualización de resultados
print(f"Ecuación de la recta: y = {slope:.4f}x + {intercept:.4f}")
print(f"Desviación estándar (sy): {sy:.4f}")
print(f"Error estándar de la estimación (sy/x): {sy_x:.4f}")
print(f"Coeficiente de determinación (r²): {r_squared:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Gráfico de dispersión y línea de regresión
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos')
plt.plot(x, y_pred, color='red', label=f'Regresión: y = {slope:.4f}x + {intercept:.4f}')
plt.title('Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()

# Análisis adicional: tabla de valores observados vs predichos
print("\nTabla de valores:")
print("X\tY (obs)\tY (pred)\tResiduo")
for i in range(len(x)):
    print(f"{x[i]}\t{y[i]}\t{y_pred[i]:.4f}\t{residuos[i]:.4f}")