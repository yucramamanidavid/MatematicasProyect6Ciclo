from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import io

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Detalles de Cada Iteración', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_plot(self, x, y, title):
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label='f(x)')
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        self.image(buf, x=10, y=None, w=180)
        buf.close()

def create_pdf(filename):
    pdf = PDF()
    pdf.add_page()
    
    # Método de Bisección
    pdf.chapter_title('Método de Bisección')
    pdf.chapter_body(
        "1. **Valores Iniciales**\n"
        "   - $x_l$ (límite inferior) se inicializa en 5.\n"
        "   - $x_u$ (límite superior) se inicializa en 10.\n"
        "\n"
        "2. **Cálculo de $x_r$ (Punto Medio)**\n"
        "   En cada iteración, el punto medio $x_r$ se calcula como:\n"
        "   $$x_r = \\frac{x_l + x_u}{2}$$\n"
        "   Este punto medio es una aproximación de la raíz. Dependiendo del signo de $f(x_r)$, decidimos si la raíz está en el intervalo $[x_l, x_r]$ o $[x_r, x_u]$.\n"
        "\n"
        "3. **Actualización de $x_l$ y $x_u$**\n"
        "   - Si $f(x_l) \\times f(x_r) < 0$, significa que la raíz está en el intervalo $[x_l, x_r]$, por lo que actualizamos $x_u = x_r$.\n"
        "   - Si $f(x_l) \\times f(x_r) > 0$, la raíz está en el intervalo $[x_r, x_u]$, por lo que actualizamos $x_l = x_r$.\n"
        "\n"
        "4. **Cálculo del Error Estimado ($e_a$)**\n"
        "   El error estimado se calcula a partir de la diferencia relativa entre la aproximación actual ($x_r$) y la aproximación anterior ($x_{r,\\text{anterior}}$):\n"
        "   $$e_a = \\left| \\frac{x_r - x_{r,\\text{anterior}}}{x_r} \\right| \\times 100$$\n"
        "   Nota: En la primera iteración, no hay error estimado porque no hay una iteración anterior con la que comparar.\n"
        "\n"
        "5. **Cálculo del Error Verdadero ($e_t$)**\n"
        "   El error verdadero se calcula en función de la diferencia entre la raíz exacta ($x_{\\text{exacta}}$) y la aproximación actual ($x_r$):\n"
        "   $$e_t = \\left| \\frac{x_{\\text{exacta}} - x_r}{x_{\\text{exacta}}} \\right| \\times 100$$\n"
        "   La raíz exacta $x_{\\text{exacta}}$ se obtiene previamente usando la fórmula cuadrática.\n"
    )

    # Método de Falsa Posición
    pdf.chapter_title('Método de Falsa Posición')
    pdf.chapter_body(
        "1. **Determinación Analítica**\n"
        "   Para encontrar la raíz real analíticamente, buscamos el valor de $x$ donde $f(x) = 0$:\n"
        "   $$0.8 - 0.3x = 0$$\n"
        "   Resolviendo para $x$:\n"
        "   $$x = \\frac{0.8}{0.3} \\approx 2.6667$$\n"
        "   Por lo tanto, la raíz real de $f(x)$ es aproximadamente 2.6667.\n"
        "\n"
        "2. **Determinación Gráfica**\n"
        "   Para determinar la raíz gráfica de $f(x)$, grafica la función $f(x)$ y observa el punto donde cruza el eje $x$.\n"
        "\n"
        "3. **Método de la Falsa Posición**\n"
        "   El método de la falsa posición se basa en la intersección de las líneas secantes. Vamos a realizar tres iteraciones con valores iniciales $x_1 = 1$ y $x_2 = 3$.\n"
        "\n"
        "   - **Primera Iteración:**\n"
        "     - Evaluamos:\n"
        "       $$f(1) = \\frac{0.8 - 0.3 \\cdot 1}{1} = 0.5$$\n"
        "       $$f(3) = \\frac{0.8 - 0.3 \\cdot 3}{3} = -0.1$$\n"
        "     - Cálculo del nuevo punto de intersección:\n"
        "       $$x_{\\text{new}} = x_1 - \\frac{f(x_1) \\cdot (x_2 - x_1)}{f(x_2) - f(x_1)}$$\n"
        "       $$x_{\\text{new}} = 1 - \\frac{0.5 \\cdot (3 - 1)}{-0.1 - 0.5} \\approx 1.3333$$\n"
        "     - Evaluamos:\n"
        "       $$f(1.3333) \\approx 0.0667$$\n"
        "     - Actualizamos el intervalo:\n"
        "       Nuevo intervalo: $[1.3333, 3]$\n"
        "\n"
        "   - **Segunda Iteración:**\n"
        "     - Evaluamos:\n"
        "       $$f(1.3333) \\approx 0.0667$$\n"
        "       $$f(3) = -0.1$$\n"
        "     - Cálculo del nuevo punto de intersección:\n"
        "       $$x_{\\text{new}} \\approx 1.4750$$\n"
        "     - Evaluamos:\n"
        "       $$f(1.4750) \\approx -0.0033$$\n"
        "     - Actualizamos el intervalo:\n"
        "       Nuevo intervalo: $[1.4750, 3]$\n"
        "\n"
        "   - **Tercera Iteración:**\n"
        "     - Evaluamos:\n"
        "       $$f(1.4750) \\approx -0.0033$$\n"
        "       $$f(3) = -0.1$$\n"
        "     - Cálculo del nuevo punto de intersección:\n"
        "       $$x_{\\text{new}} \\approx 1.5225$$\n"
        "     - Evaluamos:\n"
        "       $$f(1.5225) \\approx 0.0095$$\n"
        "     - Actualizamos el intervalo:\n"
        "       Nuevo intervalo: $[1.5225, 3]$\n"
    )

    # Agregar gráficos
    # Ejemplo: Gráfico para el Método de Bisección
    x = np.linspace(0, 10, 400)
    y = np.sin(x)
    pdf.add_plot(x, y, 'Ejemplo de Gráfico para el Método de Bisección')

    pdf.output(filename)

# Llamar a la función para crear el PDF
create_pdf('detalles_iteraciones.pdf')
