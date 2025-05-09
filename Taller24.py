import matplotlib.pyplot as plt

def multiplicar_polinomios(p1, p2):
    grado = len(p1) + len(p2) - 2
    resultado = [0] * (grado + 1)

    for indice1, valor1 in enumerate(p1):
        for indice2, valor2 in enumerate(p2):
            resultado[indice1 + indice2] += valor1 * valor2
    return resultado

def escalar_polinomio(p, escalar):
    return [coef * escalar for coef in p]
def sumar_polinomios(p1, p2):
    grado = max(len(p1), len(p2))
    resultado = [0] * grado

    for i in range(len(p1)):
        resultado[i] += p1[i]
    for i in range(len(p2)):
        resultado[i] += p2[i]

    return resultado

def evaluar_polinomio(p, x_val):
    resultado = 0
    for i, coef in enumerate(p):
        resultado += coef * (x_val ** i)
    return resultado

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 0.5, -2, -3.5, 0.5]

    n = len(x)
    polinomio_total = [0]

    for i in range(n):
        numerador = [1]
        denominador = 1

        for j in range(n):
            if j != i:
                numerador = multiplicar_polinomios(numerador, [-x[j], 1])
                denominador *= (x[i] - x[j])

        Li = escalar_polinomio(numerador, 1 / denominador)
        termino = escalar_polinomio(Li, y[i])
        polinomio_total = sumar_polinomios(polinomio_total, termino)

    polinomio_redondeado = [round(coef, 3) for coef in polinomio_total]

    print("Coeficientes del polinomio resultante (grado 0 hacia arriba, redondeados):")
    print(polinomio_redondeado)

    x_grafica = [i / 10 for i in range(10, 51)]  
    y_grafica = [evaluar_polinomio(polinomio_total, xi) for xi in x_grafica]

    plt.figure(figsize=(8, 6))
    plt.plot(x_grafica, y_grafica, label='Polinomio de Lagrange', color='blue')
    plt.scatter(x, y, color='red', label='Puntos dados', zorder=5)
    plt.title('Interpolación de Lagrange ')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
