from flask import Flask, request, render_template
import numpy as np
from scipy.optimize import bisect, newton, brentq
from sympy import symbols, diff, lambdify

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

def eval_func(func_str, x):
    return eval(func_str)

def eval_derivative(func_str, x):
    x_sym = symbols('x')
    func_sym = eval(func_str, {'x': x_sym})
    df_dx_sym = diff(func_sym, x_sym)
    df_dx = lambdify(x_sym, df_dx_sym, 'numpy')
    return df_dx(x)

def metodo_biseccion(func, xl, xu, tol, max_iter):
    a = xl
    b = xu
    iteraciones = []
    if func(a) * func(b) > 0:
        raise ValueError("No hay raíces en el intervalo proporcionado.")
    
    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append({'iter': i, 'a': a, 'b': b, 'c': c, 'f(c)': func(c)})
        if abs(func(c)) < tol:
            return c, iteraciones
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, iteraciones

def metodo_falsa_posicion(func, xl, xu, tol, max_iter):
    a = xl
    b = xu
    iteraciones = []
    if func(a) * func(b) > 0:
        raise ValueError("No hay raíces en el intervalo proporcionado.")
    
    for i in range(max_iter):
        c = b - func(b) * (a - b) / (func(a) - func(b))
        iteraciones.append({'iter': i, 'a': a, 'b': b, 'c': c, 'f(c)': func(c)})
        if abs(func(c)) < tol:
            return c, iteraciones
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, iteraciones

def metodo_newton_raphson(func, df, x0, tol, max_iter):
    x = x0
    iteraciones = []
    for i in range(max_iter):
        fx = func(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivada cero en x = {}".format(x))
        x_new = x - fx / dfx
        iteraciones.append({'iter': i, 'x': x, 'f(x)': fx, 'f\'(x)': dfx})
        if abs(x_new - x) < tol:
            return x_new, iteraciones
        x = x_new
    return x, iteraciones

def metodo_secantes(func, x0, x1, tol, max_iter):
    iteraciones = []
    for i in range(max_iter):
        f0 = func(x0)
        f1 = func(x1)
        if f1 == f0:
            raise ValueError("Error: f(x0) == f(x1), división por cero.")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        iteraciones.append({'iter': i, 'x0': x0, 'x1': x1, 'x2': x2, 'f(x2)': func(x2)})
        if abs(x2 - x1) < tol:
            return x2, iteraciones
        x0, x1 = x1, x2
    return x2, iteraciones

def metodo_punto_fijo(g, x0, tol, max_iter):
    x = x0
    iteraciones = []
    for i in range(max_iter):
        x_new = g(x)
        iteraciones.append({'iter': i, 'x': x, 'g(x)': x_new})
        if abs(x_new - x) < tol:
            return x_new, iteraciones
        x = x_new
    return x, iteraciones

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func_str = request.form['func']
        xl = float(request.form['xl'])
        xu = float(request.form['xu'])
        tol = float(request.form['tol'])
        max_iter = int(request.form['max_iter'])
        metodo = request.form['metodo']
        
        results = {}

        try:
            if metodo == "bisección":
                root, iteraciones = metodo_biseccion(lambda x: eval_func(func_str, x), xl, xu, tol, max_iter)
                results['root'] = root
                results['method'] = 'Bisección'
                results['iteraciones'] = iteraciones

            elif metodo == "falsa_posicion":
                root, iteraciones = metodo_falsa_posicion(lambda x: eval_func(func_str, x), xl, xu, tol, max_iter)
                results['root'] = root
                results['method'] = 'Falsa Posición'
                results['iteraciones'] = iteraciones

            elif metodo == "newton_raphson":
                df_str = request.form['dfunc']
                df_func = lambda x: eval_derivative(df_str, x)
                root, iteraciones = metodo_newton_raphson(lambda x: eval_func(func_str, x), df_func, xl, tol, max_iter)
                results['root'] = root
                results['method'] = 'Newton-Raphson'
                results['iteraciones'] = iteraciones

            elif metodo == "secantes":
                x1 = xl
                x0 = xu
                root, iteraciones = metodo_secantes(lambda x: eval_func(func_str, x), x0, x1, tol, max_iter)
                results['root'] = root
                results['method'] = 'Secantes'
                results['iteraciones'] = iteraciones

            elif metodo == "punto_fijo":
                g_str = request.form['gfunc']
                g_func = lambda x: eval_func(g_str, x)
                root, iteraciones = metodo_punto_fijo(g_func, xl, tol, max_iter)
                results['root'] = root
                results['method'] = 'Punto Fijo'
                results['iteraciones'] = iteraciones

            # Guardar gráfico
            if 'iteraciones' in results:
                data = {'x': [item['c'] for item in results['iteraciones']],
                        'y': [item['f(c)'] for item in results['iteraciones']]}
                save_plot(data, 'graph.png')

            return render_template('resultados.html', resultados=results)
        except Exception as e:
            return str(e)

    return render_template('index.html')

def save_plot(data, filename):
    plt.figure()
    plt.plot(data['x'], data['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico de Resultados')
    plt.savefig(f'static/{filename}')
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
