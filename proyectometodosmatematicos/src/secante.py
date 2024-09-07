# src/secante.py
def secante(f, x0, x1, tol=1e-5, max_iter=100):
    iteraciones = []
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < 1e-10:
            raise ValueError("La diferencia en los valores de la función es demasiado pequeña, el método puede no converger.")
        
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        iteraciones.append((i, x0, x1, x_new, f(x_new)))
        
        if abs(x_new - x1) < tol:
            return x_new, iteraciones
        
        x0 = x1
        x1 = x_new
        
    return x_new, iteraciones
