import math

def calcular_coseno_aproximado(x, epsilon_s):
    valor_estimado = 1.0  
    termino = 1.0  
    n = 1  
    iteraciones = 0  
    error_relativo = 100.0  
    
    while error_relativo > epsilon_s:
        iteraciones += 1
        termino *= -x**2 / (2 * n * (2 * n - 1))  
        valor_estimado += termino
        error_relativo = abs((math.cos(x) - valor_estimado) / math.cos(x)) * 100
        n += 1

    return valor_estimado, error_relativo, iteraciones

x = float(input("Ingrese el valor en radianes (x): "))
epsilon_s = float(input("Ingrese el valor del criterio de error (εs): "))

valor_estimado, error_relativo, iteraciones = calcular_coseno_aproximado(x, epsilon_s)

print(f"\nValor estimado de cos({x}) = {valor_estimado:.8f}")
print(f"Error relativo aproximado = {error_relativo:.8f}%")
print(f"Número de iteraciones realizadas: {iteraciones}")
