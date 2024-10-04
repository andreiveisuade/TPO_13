from datetime import datetime
import json

def cargar_contribuyentes():
    try:
        with open("contribuyentes.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: archivo JSON corrupto o no encontrado.")
        return []

def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

def validar_edad(edad):
    return isinstance(edad, int) and 0 < edad < 120

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_monto(monto):
    return isinstance(monto, float) and monto >= 0

def validar_contribuyente(contribuyente):
    errores = []
    if not validar_dni(contribuyente["dni"]):
        errores.append("DNI inválido.")
    if not contribuyente["nombre"]:
        errores.append("Nombre es requerido.")
    if not contribuyente["apellido"]:
        errores.append("Apellido es requerido.")
    if not validar_edad(contribuyente["edad"]):
        errores.append("Edad inválida.")
    if not validar_fecha(contribuyente["fecha"]):
        errores.append("Fecha inválida. Debe tener el formato DD/MM/AAAA.")
    if not validar_monto(contribuyente["monto"]):
        errores.append("Monto inválido.")
    return errores