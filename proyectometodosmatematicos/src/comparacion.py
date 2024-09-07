# src/comparacion.py
def comparar_todos_los_metodos(f, df, g, a, b, x0, x1, tol=1e-5, max_iter=100):
    from biseccion import biseccion
    from falsa_posicion import falsa_posicion
    from newton_raphson import newton_raphson
    from secante import secante
    from punto_fijo import punto_fijo

    raiz_biseccion, iteraciones_biseccion = biseccion(f, a, b, tol, max_iter)
    raiz_falsa_posicion, iteraciones_falsa_posicion = falsa_posicion(f, a, b, tol, max_iter)
    raiz_newton, iteraciones_newton = newton_raphson(f, df, x0, tol, max_iter)
    raiz_secante, iteraciones_secante = secante(f, x0, x1, tol, max_iter)
    raiz_punto_fijo, iteraciones_punto_fijo = punto_fijo(g, x0, tol, max_iter)

    comparacion = {
        "biseccion": {
            "raiz": raiz_biseccion,
            "iteraciones": len(iteraciones_biseccion)
        },
        "falsa_posicion": {
            "raiz": raiz_falsa_posicion,
            "iteraciones": len(iteraciones_falsa_posicion)
        },
        "newton_raphson": {
            "raiz": raiz_newton,
            "iteraciones": len(iteraciones_newton)
        },
        "secante": {
            "raiz": raiz_secante,
            "iteraciones": len(iteraciones_secante)
        },
        "punto_fijo": {
            "raiz": raiz_punto_fijo,
            "iteraciones": len(iteraciones_punto_fijo)
        }
    }

    return comparacion
