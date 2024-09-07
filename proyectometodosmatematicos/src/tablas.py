import pandas as pd

def generar_tabla(iteraciones, metodo):
    df = pd.DataFrame(iteraciones)
    print(f"\nTabla de {metodo}:")
    print(df)

# Puedes tener una función específica para cada método si es necesario
def generar_tabla_biseccion(iteraciones):
    generar_tabla(iteraciones, "Bisección")

def generar_tabla_falsa_posicion(iteraciones):
    generar_tabla(iteraciones, "Falsa Posición")

def generar_tabla_newton_raphson(iteraciones):
    generar_tabla(iteraciones, "Newton-Raphson")

def generar_tabla_secantes(iteraciones):
    generar_tabla(iteraciones, "Secantes")

def generar_tabla_punto_fijo(iteraciones):
    generar_tabla(iteraciones, "Punto Fijo")
