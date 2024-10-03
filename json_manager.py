import json
from utils import cargar_contribuyentes

def guardar_contribuyente(contribuyente):
    contribuyentes = cargar_contribuyentes()
    
    contribuyentes.append(contribuyente)

    try:
        with open("contribuyentes.json", "w") as file:
            json.dump(contribuyentes, file)
    except Exception as e:
        print(f"Error al guardar el contribuyente: {e}")