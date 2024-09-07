# src/newton_raphson.py
def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    iteraciones = []
    x = x0
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-10:
            raise ValueError("La derivada es muy pequeña, el método puede no converger.")
        
        x_new = x - fx / dfx
        iteraciones.append((i, x, fx, dfx, x_new))
        
        if abs(x_new - x) < tol:
            return x_new, iteraciones
        
        x = x_new
        
    return x, iteraciones
