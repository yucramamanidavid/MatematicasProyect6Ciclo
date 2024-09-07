from flask import Flask, render_template, request, jsonify
import time
from utils import (bisection, false_position, newton_raphson, secant, fixed_point, plot_graph, compare_methods)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func = request.form['func']
        x0 = float(request.form['x0'])
        x1 = float(request.form['x1'])
        tol = float(request.form['tol'])
        max_iter = int(request.form['max_iter'])
        method = request.form['method']

        start_time = time.time()
        results = []
        if method == 'Bisection':
            results = bisection(func, x0, x1, tol, max_iter)
        elif method == 'False Position':
            results = false_position(func, x0, x1, tol, max_iter)
        elif method == 'Newton-Raphson':
            results = newton_raphson(func, x0, tol, max_iter)
        elif method == 'Secant':
            results = secant(func, x0, x1, tol, max_iter)
        elif method == 'Fixed Point':
            results = fixed_point(func, x0, tol, max_iter)
        exec_time = time.time() - start_time

        graph = plot_graph(func, x0, x1)
        comparison = None  # Aquí podrías incluir la comparación si es necesario

        return render_template('index.html', results=results, time=exec_time, graph=graph, comparison=comparison, method=method)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
