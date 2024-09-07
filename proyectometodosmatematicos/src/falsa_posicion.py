# src/falsa_posicion.py
def falsa_posicion(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")
    
    iteraciones = []
    for i in range(max_iter):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        iteraciones.append((i, a, b, c, f(c)))
        
        if f(c) == 0 or abs(f(c)) < tol:
            return c, iteraciones
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
    return c, iteraciones
