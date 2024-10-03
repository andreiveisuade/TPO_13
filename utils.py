import re  # Para validación de expresiones regulares
import json

def cargar_contribuyentes():
    try:
        with open("contribuyentes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def validar_dni(dni):
    # Asumiendo que el DNI debe ser un número y tener 8 dígitos
    return dni.isdigit() and len(dni) == 8

def validar_edad(edad):
    # Verifica que la edad esté en un rango razonable
    return isinstance(edad, int) and 0 < edad < 120

def validar_fecha(fecha):
    # Aquí podrías implementar un formato de fecha (DD/MM/AAAA)
    try:
        dia, mes, año = map(int, fecha.split('/'))
        return 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= año <= 2100
    except ValueError:
        return False

def validar_monto(monto):
    # Verifica que el monto sea un número positivo
    return isinstance(monto, float) and monto >= 0