import tkinter as tk
from tkinter import messagebox

# Resolver sistema lineal por eliminación de Gauss
def resolver_sistema(A, B):
    n = len(B)
    for i in range(n):
        for j in range(i+1, n):
            if A[i][i] == 0:
                continue
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]
    x = [0] * n
    for i in range(n-1, -1, -1):
        suma = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (B[i] - suma) / A[i][i]
    return x

def calcular_coeficientes(X, Y, grado):
    n = len(X)
    A = [[sum(x**(i+j) for x in X) for j in range(grado+1)] for i in range(grado+1)]
    B = [sum(Y[k] * (X[k]**i) for k in range(n)) for i in range(grado+1)]
    return resolver_sistema(A, B)

def calcular_r2(X, Y, coef):
    y_prom = sum(Y) / len(Y)
    ss_tot = sum((y - y_prom)**2 for y in Y)
    ss_res = sum((y - evaluar_pol(coef, x))**2 for x, y in zip(X, Y))
    return 1 - ss_res / ss_tot

def evaluar_pol(coef, x):
    return sum(c * (x ** i) for i, c in enumerate(coef))

# Escalar puntos para el canvas
def escalar_puntos(X, Y, ancho, alto, margen=40):
    min_x, max_x = min(X), max(X)
    min_y, max_y = min(Y), max(Y)
    def escalar(x, y):
        x_esc = margen + (x - min_x) / (max_x - min_x) * (ancho - 2 * margen)
        y_esc = alto - (margen + (y - min_y) / (max_y - min_y) * (alto - 2 * margen))
        return x_esc, y_esc
    return [escalar(x, y) for x, y in zip(X, Y)]

# Dibujar resultados en canvas
def dibujar(canvas, X, Y, coef, grado, r2):
    canvas.delete("all")
    ancho, alto = canvas.winfo_width(), canvas.winfo_height()

    puntos_escalados = escalar_puntos(X, Y, ancho, alto)
    for x, y in puntos_escalados:
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="blue")

    min_x, max_x = min(X), max(X)
    paso = (max_x - min_x) / 200
    puntos_curva = [(x, evaluar_pol(coef, x)) for x in frange(min_x, max_x, paso)]
    puntos_canvas = escalar_puntos([x for x, _ in puntos_curva], [y for _, y in puntos_curva], ancho, alto)
    
    for i in range(len(puntos_canvas) - 1):
        x1, y1 = puntos_canvas[i]
        x2, y2 = puntos_canvas[i+1]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    eq = " + ".join(f"{c:.2f}x^{i}" for i, c in enumerate(coef))
    canvas.create_text(10, 10, anchor="nw", text=f"Grado {grado}:\n{eq}\nR² = {r2:.4f}", fill="black", font=("Arial", 10), justify="left")

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

def realizar_regresion(X, Y, canvas):
    grado = 1
    while True:
        coef = calcular_coeficientes(X, Y, grado)
        r2 = calcular_r2(X, Y, coef)
        dibujar(canvas, X, Y, coef, grado, r2)
        if r2 >= 0.95 or grado >= 10:
            break
        grado += 1

# Interfaz gráfica
def on_click():
    try:
        texto = entrada.get("1.0", tk.END).strip()
        puntos = [tuple(map(float, linea.split(','))) for linea in texto.split('\n') if linea]
        if len(puntos) < 6:
            messagebox.showerror("Error", "Debe ingresar al menos 6 puntos.")
            return
        X, Y = zip(*puntos)
        realizar_regresion(list(X), list(Y), canvas)
    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

root = tk.Tk()
root.title("Regresión Polinomial sin librerías")

tk.Label(root, text="Ingresa puntos (x,y) uno por línea:").pack()
entrada = tk.Text(root, height=8, width=40)
entrada.pack()

tk.Button(root, text="Calcular regresión", command=on_click).pack()

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

root.mainloop()
