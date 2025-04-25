import numpy as np
from scipy.optimize import curve_fit

# Datos
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4.5, 6.5, 7.5, 8.0, 8.4, 8.8, 9.0, 9.3])

# Función para calcular R²
def r2(y_real, y_pred):
    Sr = np.sum((y_real - y_pred)**2)
    St = np.sum((y_real - np.mean(y_real))**2)
    return 1 - Sr / St

# --- Modelo de Potencias: y = a * x^b ---
ln_x = np.log(x)
ln_y = np.log(y)
A = np.vstack([ln_x, np.ones(len(ln_x))]).T
b_pot, ln_a_pot = np.linalg.lstsq(A, ln_y, rcond=None)[0]
a_pot = np.exp(ln_a_pot)
y_pot = a_pot * x**b_pot
r2_pot = r2(y, y_pot)

print("Modelo de Potencias:")
print(f"  y = {a_pot:.4f} * x^{b_pot:.4f}")
print(f"  R² = {r2_pot:.4f}\n")

# --- Modelo de Razón de Crecimiento: y = a / (x^b + x) ---
def razon_crecimiento(x, a, b):
    return a / (x**b + x)

params, _ = curve_fit(razon_crecimiento, x, y, p0=[10, 1])
a_rc, b_rc = params
y_rc = razon_crecimiento(x, a_rc, b_rc)
r2_rc = r2(y, y_rc)

print("Modelo de Razón de Crecimiento:")
print(f"  y = {a_rc:.4f} / (x^{b_rc:.4f} + x)")
print(f"  R² = {r2_rc:.4f}")
