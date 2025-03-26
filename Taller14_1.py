import numpy as np

def producto_escalar():
    while True:
        try:
            n = int(input("Ingrese la longitud de los vectores (n): "))
            if n > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
    vector1 = np.random.randint(-10, 11, n)
    vector2 = np.random.randint(-10, 11, n)
    producto = np.dot(vector1, vector2)
    print("\nVector 1:", vector1)
    print("Vector 2:", vector2)
    print("Producto escalar:", producto)

producto_escalar()