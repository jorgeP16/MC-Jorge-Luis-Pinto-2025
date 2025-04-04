def crear_matriz(filas, columnas, valores=None):
    if valores:
        return [valores[i*columnas:(i+1)*columnas] for i in range(filas)]
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]
def crear_identidad(n):
    matriz = crear_matriz(n, n)
    for i in range(n):
        matriz[i][i] = 1.0
    return matriz
def imprimir_matriz(matriz, label="Matriz"):
    print(f"{label}:")
    for fila in matriz:
        print("[", end=" ")
        for valor in fila:
            print(f"{valor:8.4f}", end=" ")
        print("]")
    print()
def copiar_matriz(matriz):
    return [fila[:] for fila in matriz]
def gauss_jordan_inverse(matriz):
    n = len(matriz)
    aumentada = []
    for i in range(n):
        fila = matriz[i].copy()
        identidad_fila = [0.0] * n
        identidad_fila[i] = 1.0
        fila.extend(identidad_fila)
        aumentada.append(fila)
    for i in range(n):
        max_row = i
        max_val = abs(aumentada[i][i])
        for j in range(i + 1, n):
            if abs(aumentada[j][i]) > max_val:
                max_val = abs(aumentada[j][i])
                max_row = j
        if max_row != i:
            aumentada[i], aumentada[max_row] = aumentada[max_row], aumentada[i]
        if abs(aumentada[i][i]) < 1e-10:
            raise ValueError("La matriz no es invertible")
        pivot = aumentada[i][i]
        for j in range(2*n):
            aumentada[i][j] /= pivot
        for j in range(n):
            if j != i:
                factor = aumentada[j][i]
                for k in range(2*n):
                    aumentada[j][k] -= factor * aumentada[i][k]
    inversa = []
    for i in range(n):
        inversa.append(aumentada[i][n:])
    return inversa
def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    resultado = crear_matriz(filas_A, columnas_B)
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0.0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            resultado[i][j] = suma
    return resultado
def es_aproximadamente_identidad(matriz, tolerancia=1e-10):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j:
                if abs(matriz[i][j] - 1.0) > tolerancia:
                    return False
            else:
                if abs(matriz[i][j]) > tolerancia:
                    return False
    return True
def verificar_inversa(matriz, inversa):
    producto = multiplicar_matrices(matriz, inversa)
    es_identidad = es_aproximadamente_identidad(producto)
    return es_identidad, producto
def main():
    A = [
        [3.0, 2.0, 2.0],
        [3.0, 1.0, -3.0],
        [1.0, 0.0, -2.0]
    ]
    B = [
        [1.0, 2.0, 0.0, 4.0],
        [2.0, 0.0, -1.0, -2.0],
        [1.0, 1.0, -1.0, 0.0],
        [0.0, 4.0, 1.0, 0.0]
    ]
    print("=" * 60)
    print("CÁLCULO DE INVERSAS MEDIANTE ELIMINACIÓN DE GAUSS-JORDAN")
    print("=" * 60)
    print("\nPROCESANDO MATRIZ A")
    print("-" * 30)
    imprimir_matriz(A, "Matriz A")
    try:
        A_inv = gauss_jordan_inverse(A)
        imprimir_matriz(A_inv, "Inversa de A")
        es_valida, producto = verificar_inversa(A, A_inv)
        imprimir_matriz(producto, "A × A⁻¹")
        if es_valida:
            print("✓ Verificación exitosa: A × A⁻¹ ≈ I\n")
        else:
            print("✗ Verificación fallida: A × A⁻¹ ≠ I\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    print("\nPROCESANDO MATRIZ B")
    print("-" * 30)
    imprimir_matriz(B, "Matriz B")
    try:
        B_inv = gauss_jordan_inverse(B)
        imprimir_matriz(B_inv, "Inversa de B")
        es_valida, producto = verificar_inversa(B, B_inv)
        imprimir_matriz(producto, "B × B⁻¹")
        if es_valida:
            print("✓ Verificación exitosa: B × B⁻¹ ≈ I\n")
        else:
            print("✗ Verificación fallida: B × B⁻¹ ≠ I\n")
    except ValueError as e:
        print(f"Error: {e}\n")
if __name__ == "__main__":
    main()