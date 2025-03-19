import numpy as np
import sympy as sp
import math

def calcular_error_propagado(funcion_simbolica, valor_x, error_x):
    x = sp.Symbol('x')
    
    derivada = sp.diff(funcion_simbolica, x)
    
    valor_funcion = float(funcion_simbolica.subs(x, valor_x))
    valor_derivada = float(derivada.subs(x, valor_x))
    
    error_propagado = abs(valor_derivada) * error_x
    
    return valor_funcion, error_propagado, valor_derivada
def resolver_problema1():
    x = sp.Symbol('x')
    funcion = 1.1*x**4 - 1.9*x**3 + 1.2*x**2 - 2*x + 4
    valor_x = 1.4
    error_x = 0.05
    valor_f, error_f, derivada = calcular_error_propagado(funcion, valor_x, error_x)
    
    print("\nProblema 1:")
    print(f"Función: f(x) = 1,1x⁴ - 1,9x³ + 1,2x² - 2x + 4")
    print(f"Valor de x = {valor_x} ± {error_x}")
    print(f"Derivada f'(x) = {sp.expand(sp.diff(funcion, x))}")
    print(f"f'({valor_x}) = {derivada}")
    print(f"f({valor_x}) = {valor_f}")
    print(f"Error propagado Δf = |f'(x)| · Δx = {abs(derivada)} · {error_x} = {error_f}")
    print(f"Resultado final: f({valor_x} ± {error_x}) = {valor_f} ± {error_f}")

def resolver_problema2():
    x = sp.Symbol('x')
    funcion = sp.cos(x) * sp.ln(2*x)
    valor_x = np.pi/3
    error_x = 0.005
    
    valor_f, error_f, derivada = calcular_error_propagado(funcion, valor_x, error_x)
    
    print("\nProblema 2:")
    print(f"Función: f(x) = cos(x) * ln(2x)")
    print(f"Valor de x = π/3 ± {error_x}")
    print(f"Valor de x ≈ {valor_x:.6f} ± {error_x}")
    print(f"Derivada f'(x) = {sp.diff(funcion, x)}")
    print(f"f'(π/3) = {derivada}")
    print(f"f(π/3) = {valor_f}")
    print(f"Error propagado Δf = |f'(x)| · Δx = {abs(derivada)} · {error_x} = {error_f}")
    print(f"Resultado final: f(π/3 ± {error_x}) = {valor_f} ± {error_f}")

if __name__ == "__main__":
    print("Calculadora de Propagación de Errores")
    print("=====================================")
    
    resolver_problema1()
    resolver_problema2()