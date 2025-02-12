def es_subconjunto(U, A):
    return set(A).issubset(set(U))

cardinalidad_U = int(input("Introduce la cardinalidad del conjunto U: "))
U = []
for i in range(cardinalidad_U):
    elemento = input(f"Introduce el elemento {i+1} del conjunto U: ")
    U.append(elemento)

cardinalidad_A = int(input("Introduce la cardinalidad del conjunto A: "))
A = []
for i in range(cardinalidad_A):
    elemento = input(f"Introduce el elemento {i+1} del conjunto A: ")
    A.append(elemento)

if es_subconjunto(U, A):
    print("A es un subconjunto de U.")

    interseccion_U_A = set(U).intersection(set(A))
    resultado_1 = interseccion_U_A.union(set(A))
    print(f"(U ∩ A) ∪ A: {resultado_1}")
    
    interseccion_A_A = set(A).intersection(set(A))
    resultado_2 = set(U).difference(interseccion_A_A)
    print(f"U − (A ∩ A): {resultado_2}")
    
    diferencia_simetrica = set(U).symmetric_difference(set(A))
    resultado_3 = diferencia_simetrica.difference(set(A))
    print(f"U ⨁ A − A: {resultado_3}")
else:
    print("A no es un subconjunto de U. No se pueden realizar las operaciones.")
