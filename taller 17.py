import matplotlib.pyplot as plt

# Datos proporcionados
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1]

# Calcular los coeficientes manualmente
n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2 = sum(xi * xi for xi in x)

# Fórmulas para la regresión lineal por mínimos cuadrados
pendiente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
intercepto = (sum_y - pendiente * sum_x) / n

# Calcular la línea de regresión
y_pred = [pendiente * xi + intercepto for xi in x]

# Calcular el coeficiente de determinación R²
y_mean = sum(y) / n
ss_total = sum((yi - y_mean) ** 2 for yi in y)
ss_residual = sum((yi - y_pred_i) ** 2 for yi, y_pred_i in zip(y, y_pred))
r2 = 1 - (ss_residual / ss_total)

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', linewidth=2, label=f'Regresión: y = {pendiente:.4f}x + {intercepto:.4f}')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Mostrar los resultados
print(f"Ecuación de la recta: y = {pendiente:.4f}x + {intercepto:.4f}")
print(f"Coeficiente de determinación (R²): {r2:.4f}")

# Mostrar la gráfica
plt.show()