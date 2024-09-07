def biseccion(f, xl, xu, tol=1e-5, max_iter=100):
    xr = xl
    iteraciones = []
    errores = []

    for i in range(max_iter):
        xr_old = xr
        xr = (xl + xu) / 2.0
        iteraciones.append(i)
        errores.append(abs((xr - xr_old) / xr) * 100 if i > 0 else 0)

        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            break

        if abs((xr - xr_old) / xr) * 100 < tol:
            break

    return xr, iteraciones, errores

def falsa_posicion(f, a, b, tol=1e-5, max_iter=100):
    iteraciones = []
    errores = []

    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        xk = (a * fb - b * fa) / (fb - fa)
        iteraciones.append(i)
        errores.append(abs(f(xk)))

        if f(xk) == 0 or errores[-1] < tol:
            break
        elif fa * f(xk) < 0:
            b = xk
        else:
            a = xk

    return xk, iteraciones, errores
