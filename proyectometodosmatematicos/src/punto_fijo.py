# src/punto_fijo.py
def punto_fijo(g, x0, tol=1e-5, max_iter=100):
    iteraciones = []
    x = x0
    
    for i in range(max_iter):
        x_new = g(x)
        iteraciones.append((i, x, x_new))
        
        if abs(x_new - x) < tol:
            return x_new, iteraciones
        
        x = x_new
        
    return x, iteraciones
