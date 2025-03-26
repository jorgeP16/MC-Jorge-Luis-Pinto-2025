import numpy as np
import random

def operaciones_matrices():
    while True:
        operacion = input("Seleccione la operación (suma/multiplicación): ").lower()
        if operacion in ['suma', 'multiplicación']:
            break
        else:
            print("Operación no válida. Elija suma o multiplicación.")
    if operacion == 'suma':
        filas = random.randint(2, 8)
        columnas = random.randint(2, 8)
        A = np.random.randint(-10, 11, (filas, columnas))
        B = np.random.randint(-10, 11, (filas, columnas))
        
        resultado = A + B
        operacion_simbolo = '+'
    else: 
        filas_A = random.randint(2, 8)
        columnas_A = random.randint(2, 8)
        filas_B = columnas_A 
        columnas_B = random.randint(2, 8)
        
        A = np.random.randint(-10, 11, (filas_A, columnas_A))
        B = np.random.randint(-10, 11, (filas_B, columnas_B))
        
        resultado = np.dot(A, B)
        operacion_simbolo = '×'
    
    print(f"\nMatriz A:\n{A}")
    print(f"\nMatriz B:\n{B}")
    print(f"\nResultado de {operacion} ({operacion_simbolo}):\n{resultado}")
operaciones_matrices()
