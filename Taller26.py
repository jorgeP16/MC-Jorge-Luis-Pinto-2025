import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)

    def inorden(self):
        print("\nElementos del árbol en orden ascendente:")
        self._inorden_recursivo(self.raiz)
        print()

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self._inorden_recursivo(nodo_actual.derecha)

def main():
    arbol = ArbolBinarioBusqueda()
    numeros = random.sample(range(1, 101), 20)
    for numero in numeros:
        arbol.insertar(numero)

    while True:
        print("\nMenú:")
        print("1. Agregar un número al árbol")
        print("2. Buscar un número en el árbol")
        print("3. Imprimir elementos del árbol en orden ascendente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                valor = int(input("Ingrese el número que desea agregar: "))
                arbol.insertar(valor)
                print(f" El número {valor} fue agregado al árbol.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese un número entero.")
        elif opcion == '2':
            try:
                valor = int(input("Ingrese el número a buscar: "))
                if arbol.buscar(valor):
                    print(f" El número {valor} se encuentra en el árbol.")
                else:
                    print(f" El número {valor} NO se encuentra en el árbol.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese un número entero.")
        elif opcion == '3':
            arbol.inorden()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
