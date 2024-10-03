import json
from utils import cargar_contribuyentes

def guardar_contribuyente(contribuyente):
    try:
        # Cargar contribuyentes existentes
        contribuyentes = cargar_contribuyentes()
    except FileNotFoundError:
        contribuyentes = []
    
    # Añadir nuevo contribuyente
    contribuyentes.append(contribuyente)

    # Guardar de nuevo en el archivo JSON
    try:
        with open("contribuyentes.json", "w") as file:
            json.dump(contribuyentes, file)
    except Exception as e:
        print(f"Error al guardar el contribuyente: {e}")