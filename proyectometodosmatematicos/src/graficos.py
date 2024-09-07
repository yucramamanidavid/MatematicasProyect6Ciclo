import matplotlib.pyplot as plt

def plot_biseccion(x_vals, y_vals, root):
    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.axvline(x=root, color='r', linestyle='--', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Bisección')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_falsa_posicion(x_vals, y_vals, root):
    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.axvline(x=root, color='g', linestyle='--', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Falsa Posición')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_newton_raphson(x_vals, y_vals, root):
    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.axvline(x=root, color='b', linestyle='--', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Newton-Raphson')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_secantes(x_vals, y_vals, root):
    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.axvline(x=root, color='m', linestyle='--', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Secantes')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_punto_fijo(x_vals, y_vals, root):
    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.axvline(x=root, color='c', linestyle='--', label='Raíz')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método del Punto Fijo')
    plt.legend()
    plt.grid(True)
    plt.show()
