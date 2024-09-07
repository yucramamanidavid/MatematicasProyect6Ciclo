import re

def normalize_function_string(function_str):
    # Reemplazar '^' por '**' para la exponenciación
    function_str = function_str.replace('^', '**')
    
    # Insertar '*' entre números y variables, o variables adyacentes
    function_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', function_str)
    function_str = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', function_str)
    
    # Asegurarse de que la variable sea 'x'
    function_str = function_str.replace('x', 'x')
    
    return function_str

def parse_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("El valor debe ser un número válido.")
