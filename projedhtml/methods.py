import sympy as sp

def bisection_method(func, a, b, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(func))
    
    data = []
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            break
        data.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'fa': f(a),
            'fb': f(b),
            'fc': f(c),
            'error': abs(b - a)
        })
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return data

def false_position_method(func, a, b, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(func))

    data = []
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)

        data.append({
            'iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'fa': fa,
            'fb': fb,
            'fc': fc,
            'error': abs(fc)
        })

        if abs(fc) < tol:
            break

        if fa * fc < 0:
            b = c
        else:
            a = c
    
    return data

def newton_raphson_method(func, x0, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(func))
    f_prime = sp.lambdify(x, sp.sympify(func).diff(x))

    data = []
    for i in range(max_iter):
        fx0 = f(x0)
        fpx0 = f_prime(x0)
        if fpx0 == 0:
            raise ValueError("La derivada es cero, no se puede continuar.")

        x1 = x0 - fx0 / fpx0
        error = abs(x1 - x0)
        
        data.append({
            'iteration': i + 1,
            'x0': x0,
            'fx0': fx0,
            'fpx0': fpx0,
            'x1': x1,
            'error': error
        })

        if error < tol:
            break

        x0 = x1

    return data

def secant_method(func, x0, x1, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(func))

    data = []
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if fx1 - fx0 == 0:
            raise ValueError("División por cero en el método de las secantes.")

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)
        
        data.append({
            'iteration': i + 1,
            'x0': x0,
            'x1': x1,
            'fx0': fx0,
            'fx1': fx1,
            'x2': x2,
            'error': error
        })

        if error < tol:
            break

        x0, x1 = x1, x2

    return data

def fixed_point_method(func, x0, tol, max_iter):
    x = sp.symbols('x')
    g = sp.lambdify(x, sp.sympify(func))

    data = []
    for i in range(max_iter):
        x1 = g(x0)
        error = abs(x1 - x0)
        
        data.append({
            'iteration': i + 1,
            'x0': x0,
            'x1': x1,
            'error': error
        })

        if error < tol:
            break

        x0 = x1

    return data
