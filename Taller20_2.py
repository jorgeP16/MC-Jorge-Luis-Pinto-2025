import numpy as np

# Datos
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4.5, 6.5, 7.5, 8.0, 8.4, 8.8, 9.0, 9.3])

# Función para calcular R²
def r2(y_real, y_pred):
    Sr = np.sum((y_real - y_pred)**2)
    St = np.sum((y_real - np.mean(y_real))**2)
    return 1 - Sr / St

# --- Modelo Lineal: y = a*x + b ---
A = np.vstack([x, np.ones(len(x))]).T
a_lin, b_lin = np.linalg.lstsq(A, y, rcond=None)[0]
y_lin = a_lin * x + b_lin
r2_lin = r2(y, y_lin)

print("Modelo Lineal:")
print(f"  y = {a_lin:.4f} * x + {b_lin:.4f}")
print(f"  R² = {r2_lin:.4f}\n")

# --- Modelo Exponencial: y = a * exp(b * x) ---
ln_y = np.log(y)
A_exp = np.vstack([x, np.ones(len(x))]).T
b_exp, ln_a_exp = np.linalg.lstsq(A_exp, ln_y, rcond=None)[0]
a_exp = np.exp(ln_a_exp)
y_exp = a_exp * np.exp(b_exp * x)
r2_exp = r2(y, y_exp)

print("Modelo Exponencial:")
print(f"  y = {a_exp:.4f} * exp({b_exp:.4f} * x)")
print(f"  R² = {r2_exp:.4f}")
