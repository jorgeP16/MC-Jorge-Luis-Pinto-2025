import random

def generar_conjunto(cardinalidad):
    conjunto = set()
    while len(conjunto) < cardinalidad:
        conjunto.add(random.randint(0, 30))
    return conjunto
def operaciones_conjuntos():
    cardinalidad_a = int(input("Ingrese la cardinalidad del conjunto A: "))
    cardinalidad_b = int(input("Ingrese la cardinalidad del conjunto B: "))
    A = generar_conjunto(cardinalidad_a)
    B = generar_conjunto(cardinalidad_b)
    print(f"\nConjunto A: {A}")
    print(f"Conjunto B: {B}")
    print("\nOperaciones entre los conjuntos A y B:")
    union = A.union(B)
    print(f"A u B: {union}")
    interseccion = A.intersection(B)
    print(f"A ∩ B: {interseccion}")
    diferencia_a_b = A.difference(B)
    print(f"A − B: {diferencia_a_b}")
    diferencia_b_a = B.difference(A)
    print(f"B − A: {diferencia_b_a}")
    diferencia_simetrica = A.symmetric_difference(B)
    print(f"A o B: {diferencia_simetrica}")
operaciones_conjuntos()
