# src/biseccion.py
def biseccion(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")
    
    iteraciones = []
    
    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append((i, a, b, c, f(c)))

        if f(c) == 0 or (b - a) / 2 < tol:
            return c, iteraciones
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return c, iteraciones
