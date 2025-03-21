import numpy as np

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def taylor_exp_neg_x(x, x0, order):
    result = 0
    f_x0 = np.exp(-x0) 
    for n in range(order + 1):
        deriv_n = ((-1) ** n) * f_x0
        
        result += deriv_n * ((x - x0) ** n) / factorial(n)
    return result
def main():
    x = 0.805
    x0 = 0.8
    true_value = np.exp(-x)  
    print("Orden | Aproximación | Valor Real | Error Relativo (%)")
    print("-" * 60)
    for order in range(16): 
        approx = taylor_exp_neg_x(x, x0, order)
        rel_error = abs((true_value - approx) / true_value) * 100
        
        print(f"{order:5d} | {approx:.10f} | {true_value:.10f} | {rel_error:.10f}%")
if __name__ == "__main__":
    main()