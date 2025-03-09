def get_search_parameter(value):
    try:
        response = int(value)  # Intenta convertir el valor a entero
        return response
    except ValueError:
        return value