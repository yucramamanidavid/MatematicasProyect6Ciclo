import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib
matplotlib.use('Agg')  # Configura el backend no interactivo

VALOR_EXACTO = 1.234  # Cambia este valor según sea necesario

def biseccion(f, xl, xu, es=0.01, max_iter=50):
    iteraciones = []
    prev_xr = (xl + xu) / 2
    error_aprox = float('inf')
    iter_num = 0

    while iter_num < max_iter and error_aprox > es:
        xr = (xl + xu) / 2
        fxl = f(xl)
        fxu = f(xu)
        fxr = f(xr)

        if iter_num > 0:
            error_aprox = abs((xr - prev_xr) / xr) * 100
        error_verdadero = abs(xr - VALOR_EXACTO)
        
        iteraciones.append({
            'iter': iter_num + 1,
            'xl': xl,
            'xu': xu,
            'xr': xr,
            'fxl': fxl,
            'fxu': fxu,
            'fxr': fxr,
            'error_aprox': error_aprox,
            'error_verdadero': error_verdadero,
            'operacion': f'(xl + xu) / 2',
            'formula': 'xr = (xl + xu) / 2',
            'procedimiento': '1. Calcular xr como el punto medio entre xl y xu. 2. Evaluar la función en xl, xu, y xr. 3. Calcular errores y actualizar xl o xu según el signo de f(xl) * f(xr).'
        })

        if fxl * fxr < 0:
            xu = xr
        elif fxl * fxr > 0:
            xl = xr
        else:
            break
        
        prev_xr = xr
        iter_num += 1
    
    return xr, iteraciones

def falsa_posicion(f, xl, xu, es=0.01, max_iter=50):
    iteraciones = []
    prev_xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))
    error_aprox = float('inf')
    iter_num = 0

    while iter_num < max_iter and error_aprox > es:
        fxl = f(xl)
        fxu = f(xu)
        xr = (xl * fxu - xu * fxl) / (fxu - fxl)
        fxr = f(xr)

        if iter_num > 0:
            error_aprox = abs((xr - prev_xr) / xr) * 100
        error_verdadero = abs(xr - VALOR_EXACTO)
        
        iteraciones.append({
            'iter': iter_num + 1,
            'xl': xl,
            'xu': xu,
            'xr': xr,
            'fxl': fxl,
            'fxu': fxu,
            'fxr': fxr,
            'error_aprox': error_aprox,
            'error_verdadero': error_verdadero,
            'operacion': 'xr = (xl * fxu - xu * fxl) / (fxu - fxl)',
            'formula': 'xr = (xl * fxu - xu * fxl) / (fxu - fxl)',
            'procedimiento': '1. Calcular xr usando la fórmula de la falsa posición. 2. Evaluar la función en xl, xu, y xr. 3. Calcular errores y actualizar xl o xu según el signo de f(xl) * f(xr).'
        })

        if fxl * fxr < 0:
            xu = xr
        elif fxl * fxr > 0:
            xl = xr
        else:
            break
        
        prev_xr = xr
        iter_num += 1
    
    return xr, iteraciones

def plot_function(f, xl, xu, plot_path, resultados=None):
    # Generar valores x para cubrir un rango más amplio
    x_vals = np.linspace(xl - 2, xu + 2, 1000)
    y_vals = np.array([f(x) for x in x_vals])
    
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue', linewidth=2)
    
    # Añadir líneas verticales para xl y xu
    plt.axvline(x=xl, color='red', linestyle='--', label=f'xl = {xl}', linewidth=2)
    plt.axvline(x=xu, color='green', linestyle='--', label=f'xu = {xu}', linewidth=2)
    
    # Añadir puntos para cada resultado final e iteraciones
    if resultados:
        for i, paso in enumerate(resultados):
            plt.plot(paso['xr'], f(paso['xr']), 'ro', markersize=6, label=f'Iteración {i + 1}: xr = {paso["xr"]:.4f}')
            plt.annotate(f'xr = {paso["xr"]:.4f}', 
                         xy=(paso['xr'], f(paso['xr'])), 
                         xytext=(10, 10),
                         textcoords='offset points',
                         arrowprops=dict(arrowstyle='->', color='black'))

        # Marcar la raíz final
        raiz_final = resultados[-1]['xr']
        plt.plot(raiz_final, f(raiz_final), 'go', markersize=8, label=f'Raíz: xr = {raiz_final:.4f}', color='green')
    
    # Añadir líneas horizontales en la posición de la función
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Configuración adicional
    plt.title('Gráfico de la Función con Iteraciones y Raíz', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Ajustar los ejes para que se adapten a los datos
    plt.autoscale(enable=True, axis='both', tight=True)
    
    # Guardar y cerrar el gráfico
    plt.savefig(plot_path, bbox_inches='tight')
    plt.close()





#---------------------------------------------------------------------#
def create_pdf(results, plot_path, save_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Título del documento
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Resultados del Cálculo", ln=True, align='C')
    pdf.ln(10)
    
    # Tabla de resultados
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Resultados:", ln=True, align='L')
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 10)
    col_widths = [20, 30, 30, 30, 30, 30, 30, 40, 40, 60]
    headers = ["Iteración", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "Error Aproximado", "Error Verdadero", "Detalles"]
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
    pdf.ln()

    pdf.set_font("Arial", size=10)
    for paso in results:
        pdf.cell(col_widths[0], 10, str(paso['iter']), 1)
        pdf.cell(col_widths[1], 10, f"{paso['xl']:.5f}", 1)
        pdf.cell(col_widths[2], 10, f"{paso['xu']:.5f}", 1)
        pdf.cell(col_widths[3], 10, f"{paso['xr']:.5f}", 1)
        pdf.cell(col_widths[4], 10, f"{paso['fxl']:.5f}", 1)
        pdf.cell(col_widths[5], 10, f"{paso['fxu']:.5f}", 1)
        pdf.cell(col_widths[6], 10, f"{paso['fxr']:.5f}", 1)
        pdf.cell(col_widths[7], 10, f"{paso['error_aprox']:.5f}", 1)
        pdf.cell(col_widths[8], 10, f"{paso['error_verdadero']:.5f}", 1)
        pdf.cell(col_widths[9], 10, f"Iteración {paso['iter']}", 1)
        pdf.ln()

    pdf.ln(10)
    
    # Agregar gráfico
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Gráfico de la Función:", ln=True)
    pdf.ln(5)
    
    pdf.image(plot_path, x=10, y=None, w=190)
    pdf.ln(10)
    
    # Agregar detalles
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Detalles de Cada Iteración:", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", size=10)
    for paso in results:
        pdf.cell(0, 10, f"Iteración {paso['iter']}:", ln=True)
        pdf.multi_cell(0, 10, f"Operación: {paso['operacion']}")
        pdf.multi_cell(0, 10, f"Fórmula Utilizada: {paso['formula']}")
        pdf.multi_cell(0, 10, f"Procedimiento: {paso['procedimiento']}")
        pdf.ln(5)
    
    pdf.output(save_path)
