import tkinter as tk
import struct
import re

def int_to_twos_complement(num):
    return [(num >> i) & 1 for i in range(31, -1, -1)]

def evaluar_expresion(expr):
    try:
        if re.search(r'[^0-9+\-*/.]', expr):
            raise ValueError("Expresión inválida")

        expr = expr.replace("/", "//")  
        resultado = eval(expr)
        binario = int_to_twos_complement(int(resultado))

        return resultado
    except Exception as e:
        return f"Error: {str(e)}"

def calcular():
    expresion = entrada.get()
    resultado = evaluar_expresion(expresion)
    salida.config(text=f"Resultado: {resultado}")

root = tk.Tk()
root.title("Calculadora Binaria")
root.geometry("400x200")

label = tk.Label(root, text="Ingrese la operación:")
label.pack()

entrada = tk.Entry(root, width=30)
entrada.pack()

boton = tk.Button(root, text="Calcular", command=calcular)
boton.pack()

salida = tk.Label(root, text="Resultado: ")
salida.pack()

root.mainloop()

