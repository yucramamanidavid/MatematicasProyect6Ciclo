from flask import Flask, render_template, request
import math
import re
import matplotlib.pyplot as plt
import numpy as np
import io
import os

app = Flask(__name__)

def preprocess_function_str(function_str):
    function_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', function_str)
    function_str = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', function_str)
    return function_str

def biseccion(f, xl, xu, tol, max_iter):
    iteraciones = []
    errores = []
    xr = xl
    for i in range(1, max_iter + 1):
        xr_old = xr
        xr = (xl + xu) / 2.0
        iteraciones.append(xr)
        
        if i > 1:
            ea = abs((xr - xr_old) / xr) * 100
            errores.append(ea)
        else:
            errores.append(0.0)
        
        fxr = f(xr)
        fxl = f(xl)
        
        if fxl * fxr < 0:
            xu = xr
        elif fxr * f(xu) < 0:
            xl = xr
        else:
            break
        
        if i > 1 and ea < tol:
            break
    return xr, iteraciones, errores

def falsa_posicion(f, xl, xu, tol, max_iter):
    iteraciones = []
    errores = []
    xr = xl
    for i in range(1, max_iter + 1):
        xr_old = xr
        fxl = f(xl)
        fxu = f(xu)
        xr = xu - (fxu * (xl - xu)) / (fxl - fxu)
        iteraciones.append(xr)
        
        if i > 1:
            ea = abs((xr - xr_old) / xr) * 100
            errores.append(ea)
        else:
            errores.append(0.0)
        
        fxr = f(xr)
        
        if fxl * fxr < 0:
            xu = xr
        elif fxr * f(xu) < 0:
            xl = xr
        else:
            break
        
        if i > 1 and ea < tol:
            break
    return xr, iteraciones, errores

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    method = None
    iteraciones = []
    errores = []
    error_message = None
    plot_url = None
    function_plot_url = None
    function_str = None
    xl = None
    xu = None
    tol = None
    max_iter = None
    exact_value = None 
    if request.method == 'POST':
        try:
            function_str = request.form['function']
            xl = float(request.form['xl'])
            xu = float(request.form['xu'])
            tol = float(request.form['tol'])
            max_iter = int(request.form['max_iter'])
            method = request.form['method']

            function_str = preprocess_function_str(function_str)
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            
            def f(x):
                allowed_names['x'] = x
                return eval(function_str, {"__builtins__": {}}, allowed_names)

            if method == 'biseccion':
                result, iteraciones, errores = biseccion(f, xl, xu, tol, max_iter)
            elif method == 'falsa_posicion':
                result, iteraciones, errores = falsa_posicion(f, xl, xu, tol, max_iter)
            else:
                error_message = "Método seleccionado no reconocido."

            if iteraciones:
                # Crear la gráfica de iteraciones
                fig, ax = plt.subplots()
                ax.plot(iteraciones, marker='o', linestyle='-', color='b', label='Iteraciones')
                ax.set_xlabel('Número de Iteración')
                ax.set_ylabel('Valor de la Raíz')
                ax.set_title(f'Gráfico de Iteraciones - Método {method.capitalize()}')
                ax.legend()
                ax.grid(True)

                # Guardar la gráfica en el directorio estático
                plot_path = os.path.join('static', 'plot.png')
                plt.savefig(plot_path)
                plt.close()

                plot_url = '/static/plot.png'

            # Crear la gráfica de la función
            x = np.linspace(xl - 1, xu + 1, 400)
            y = np.array([f(val) for val in x])

            fig, ax = plt.subplots()
            ax.plot(x, y, label='f(x)')
            ax.axhline(0, color='black',linewidth=0.5)
            ax.axvline(0, color='black',linewidth=0.5)
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            ax.set_title('Gráfica de la Función')
            ax.grid(True)
            ax.legend()

            # Guardar la gráfica en el directorio estático
            function_plot_path = os.path.join('static', 'function_plot.png')
            plt.savefig(function_plot_path)
            plt.close()

            function_plot_url = '/static/function_plot.png'

        except (SyntaxError, NameError, ValueError) as e:
            error_message = f"Error en la función ingresada: {str(e)}"
        except Exception as e:
            error_message = f"Error: {str(e)}"

    return render_template('index.html', result=result, method=method, iteraciones=iteraciones, errores=errores, error_message=error_message, plot_url=plot_url, function_plot_url=function_plot_url, function_str=function_str, xl=xl, xu=xu, tol=tol, max_iter=max_iter)

if __name__ == '__main__':
    app.run(debug=True)
