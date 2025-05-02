import numpy as np
import matplotlib.pyplot as plt

# Datos de la tabla
X = np.array([
    [1, 0],
    [1, 0.5],
    [2, 0.5],
    [3, 1],
    [-1.5, -1.2],
    [2, 1.5],
    [3, 1.5],
    [3, 0.5]
])
y = np.array([0.2, 3, -0.8, -0.4, 3.5, 3.6, 0.5, -1])

X_design = np.column_stack((X, np.ones(X.shape[0])))

beta = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y

a1, a2, b = beta

y_pred = X_design @ beta

ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - (ss_res / ss_tot)

correlation = np.corrcoef(y, y_pred)[0, 1]

print(f"Función ajustada: y = {a1:.3f}*x1 + {a2:.3f}*x2 + {b:.3f}")
print(f"Coeficiente de determinación (R^2): {r2:.3f}")
print(f"Coeficiente de correlación: {correlation:.3f}")

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Datos')
ax.scatter(X[:, 0], X[:, 1], y_pred, color='red', label='Ajuste')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.title('Ajuste de regresión lineal')
ax.legend()
plt.show()
