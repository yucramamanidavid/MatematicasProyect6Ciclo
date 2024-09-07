from flask import Flask, render_template, request, jsonify, send_file
from sympy import symbols, lambdify, sympify
from methods import biseccion, falsa_posicion, plot_function, create_pdf
from utils import normalize_function_string, parse_float
import os

app = Flask(__name__)

x = symbols('x')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    function_str = request.form['function']
    xl = parse_float(request.form['xl'])
    xu = parse_float(request.form['xu'])
    tolerance = parse_float(request.form['tolerance'])
    max_iter = int(request.form['max_iter'])
    method = request.form['method']
    
    try:
        function_str = normalize_function_string(function_str)
        func_expr = sympify(function_str)
        f = lambdify(x, func_expr, 'numpy')

        if method == 'biseccion':
            raiz, pasos = biseccion(f, xl, xu, es=tolerance, max_iter=max_iter)
        elif method == 'falsa_posicion':
            raiz, pasos = falsa_posicion(f, xl, xu, es=tolerance, max_iter=max_iter)
        else:
            return jsonify({'error': 'Método no válido.'})

        # Generar gráfico
        plot_path = 'static/plot.png'
        plot_function(f, xl, xu, plot_path)

        # Crear PDF
        pdf_path = 'results.pdf'
        create_pdf(pasos, plot_path, pdf_path)

        return render_template('results.html', raiz=raiz, pasos=pasos, metodo=method, plot_path=plot_path)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/download_results')
def download_results():
    return send_file('results.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
