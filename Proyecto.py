import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())  
        salida.config(text=f"Resultado: {resultado}")
    except Exception:
        salida.config(text="Error: Expresión inválida")
        
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

    