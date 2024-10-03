import re  # Para validación de expresiones regulares

def validar_dni(dni):
    """Valida que el DNI sea un número de 8 dígitos."""
    return dni.isdigit() and len(dni) == 8

def validar_edad(edad):
    """Valida que la edad sea un número entero positivo."""
    return edad.isdigit() and int(edad) > 0

def validar_fecha(fecha):
    """Valida que la fecha esté en formato DD/MM/AAAA."""
    # Expresión regular para fechas en formato DD/MM/AAAA
    patron = r'^\d{2}/\d{2}/\d{4}$'
    return re.match(patron, fecha) is not None

def validar_monto(monto):
    """Valida que el monto sea un número positivo."""
    try:
        return float(monto) > 0
    except ValueError:
        return False