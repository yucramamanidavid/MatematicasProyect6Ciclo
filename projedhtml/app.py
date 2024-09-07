from flask import Flask, render_template, request, redirect, url_for, flash
from methods import (
    bisection_method, false_position_method, newton_raphson_method, 
    secant_method, fixed_point_method
)
import re
import numpy as np
import sympy as sp

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar `flash`

def is_valid_function(func):
    try:
        x = sp.symbols('x')
        sp.sympify(func)  # Verificar que la función sea válida
        return True
    except:
        return False

def validate_inputs(method, a, b, x0, tol, max_iter):
    try:
        a, b, x0, tol, max_iter = map(float, [a, b, x0, tol, max_iter])
        max_iter = int(max_iter)
        if tol <= 0 or max_iter <= 0:
            raise ValueError("La tolerancia y el número de iteraciones deben ser mayores que cero.")
        return a, b, x0, tol, max_iter
    except ValueError as e:
        raise ValueError(f"Entrada inválida: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    method = request.form['method']
    func = request.form['function']
    
    if not is_valid_function(func):
        flash('Función inválida. Asegúrate de usar una sintaxis correcta.', 'error')
        return redirect(url_for('index'))

    try:
        a = request.form.get('a', 0)
        b = request.form.get('b', 0)
        x0 = request.form.get('x0', 0)
        tol = request.form['tolerance']
        max_iter = request.form['maxIterations']
        
        a, b, x0, tol, max_iter = validate_inputs(method, a, b, x0, tol, max_iter)
        
        result = None
        if method == 'bisection':
            result = bisection_method(func, a, b, tol, max_iter)
        elif method == 'falsePosition':
            result = false_position_method(func, a, b, tol, max_iter)
        elif method == 'newtonRaphson':
            result = newton_raphson_method(func, x0, tol, max_iter)
        elif method == 'secant':
            result = secant_method(func, a, b, tol, max_iter)
        elif method == 'fixedPoint':
            result = fixed_point_method(func, x0, tol, max_iter)
    except ValueError as e:
        flash(f'Error durante el cálculo: {e}', 'error')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Error inesperado: {e}', 'error')
        return redirect(url_for('index'))

    return render_template('results.html', result=result, method=method)

@app.route('/compare', methods=['POST'])
def compare():
    func = request.form['function']
    compare_type = request.form['compareType']

    if not is_valid_function(func):
        flash('Función inválida. Asegúrate de usar una sintaxis correcta.', 'error')
        return redirect(url_for('index'))

    try:
        a = request.form.get('a', 0)
        b = request.form.get('b', 0)
        x0 = request.form.get('x0', 0)
        tol = request.form['tolerance']
        max_iter = request.form['maxIterations']

        a, b, x0, tol, max_iter = validate_inputs('bisection', a, b, x0, tol, max_iter)
        
        results = {}
        if compare_type == 'specific':
            method1 = request.form['method1']
            method2 = request.form['method2']

            if method1 == 'bisection':
                results['bisection'] = bisection_method(func, a, b, tol, max_iter)
            elif method1 == 'falsePosition':
                results['falsePosition'] = false_position_method(func, a, b, tol, max_iter)
            elif method1 == 'newtonRaphson':
                results['newtonRaphson'] = newton_raphson_method(func, x0, tol, max_iter)
            elif method1 == 'secant':
                results['secant'] = secant_method(func, x0, request.form['x1'], tol, max_iter)
            elif method1 == 'fixedPoint':
                results['fixedPoint'] = fixed_point_method(func, x0, tol, max_iter)

            if method2 == 'bisection':
                results['bisection'] = bisection_method(func, a, b, tol, max_iter)
            elif method2 == 'falsePosition':
                results['falsePosition'] = false_position_method(func, a, b, tol, max_iter)
            elif method2 == 'newtonRaphson':
                results['newtonRaphson'] = newton_raphson_method(func, x0, tol, max_iter)
            elif method2 == 'secant':
                results['secant'] = secant_method(func, x0, request.form['x1'], tol, max_iter)
            elif method2 == 'fixedPoint':
                results['fixedPoint'] = fixed_point_method(func, x0, tol, max_iter)
        
        elif compare_type == 'all':
            # Llamar a todos los métodos y almacenar los resultados
            results['bisection'] = bisection_method(func, a, b, tol, max_iter)
            results['falsePosition'] = false_position_method(func, a, b, tol, max_iter)
            results['newtonRaphson'] = newton_raphson_method(func, x0, tol, max_iter)
            results['secant'] = secant_method(func, x0, request.form['x1'], tol, max_iter)
            results['fixedPoint'] = fixed_point_method(func, x0, tol, max_iter)

        return render_template('comparison_results.html', results=results)
    except Exception as e:
        flash(f'Ocurrió un error: {str(e)}', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
