import numpy as np
import sympy as sp
import plotly.graph_objs as go

# Métodos Numéricos

def bisection(func_str, x0, x1, tol, max_iter):
    results = []
    func = sp.lambdify(sp.symbols('x'), sp.sympify(func_str), 'numpy')
    for i in range(max_iter):
        xm = round((x0 + x1) / 2, 2)
        f_xm = func(xm)
        if abs(f_xm) < tol:
            results.append({'iteration': i + 1, 'value': round(xm, 2), 'error': round(abs(f_xm), 2)})
            break
        if func(x0) * f_xm < 0:
            x1 = xm
        else:
            x0 = xm
        error = round(abs(x1 - x0) / 2, 2)
        results.append({'iteration': i + 1, 'value': round(xm, 2), 'error': error})
        if error < tol:
            break
    return results

def false_position(func_str, x0, x1, tol, max_iter):
    results = []
    func = sp.lambdify(sp.symbols('x'), sp.sympify(func_str), 'numpy')
    for i in range(max_iter):
        f_x0, f_x1 = func(x0), func(x1)
        xm = round(x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0), 2)
        f_xm = func(xm)
        if abs(f_xm) < tol:
            results.append({'iteration': i + 1, 'value': round(xm, 2), 'error': round(abs(f_xm), 2)})
            break
        if f_x0 * f_xm < 0:
            x1 = xm
        else:
            x0 = xm
        error = round(abs(f_x1 - f_x0) / (f_x1 - f_x0), 2)
        results.append({'iteration': i + 1, 'value': round(xm, 2), 'error': error})
        if error < tol:
            break
    return results

def newton_raphson(func_str, x0, tol, max_iter):
    results = []
    x = sp.symbols('x')
    func = sp.sympify(func_str)
    func_prime = sp.diff(func, x)
    f = sp.lambdify(x, func, 'numpy')
    f_prime = sp.lambdify(x, func_prime, 'numpy')
    
    for i in range(max_iter):
        x1 = round(x0 - f(x0) / f_prime(x0), 2)
        error = round(abs(x1 - x0), 2)
        results.append({'iteration': i + 1, 'value': round(x1, 2), 'error': error})
        if error < tol:
            break
        x0 = x1
    return results

def secant(func_str, x0, x1, tol, max_iter):
    results = []
    func = sp.lambdify(sp.symbols('x'), sp.sympify(func_str), 'numpy')
    for i in range(max_iter):
        f_x0, f_x1 = func(x0), func(x1)
        x2 = round(x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0), 2)
        error = round(abs(x2 - x1), 2)
        results.append({'iteration': i + 1, 'value': round(x2, 2), 'error': error})
        if error < tol:
            break
        x0, x1 = x1, x2
    return results

def fixed_point(func_str, x0, tol, max_iter):
    results = []
    x = sp.symbols('x')
    func = sp.lambdify(x, sp.sympify(func_str), 'numpy')
    
    for i in range(max_iter):
        x1 = round(func(x0), 2)
        error = round(abs(x1 - x0), 2)
        results.append({'iteration': i + 1, 'value': round(x1, 2), 'error': error})
        if error < tol:
            break
        x0 = x1
    return results

# Función para graficar
def plot_graph(func_str, x0, x1):
    x = np.linspace(x0, x1, 400)
    y = sp.lambdify(sp.symbols('x'), sp.sympify(func_str), 'numpy')(x)

    trace = go.Scatter(x=x, y=y, mode='lines', name=func_str)
    layout = go.Layout(title='Gráfico de la Función', xaxis=dict(title='x'), yaxis=dict(title='f(x)'))
    fig = go.Figure(data=[trace], layout=layout)

    return fig.to_html(full_html=False)

# Función para comparar métodos
def compare_methods(methods_results):
    # Implementación de la comparación y generación de gráficos comparativos
    pass
