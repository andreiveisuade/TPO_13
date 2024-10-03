import json

def guardar_contribuyente(contribuyente):
    try:
        # Cargar contribuyentes existentes
        with open("contribuyentes.json", "r") as file:
            contribuyentes = json.load(file)
    except FileNotFoundError:
        contribuyentes = []
    
    # Añadir nuevo contribuyente
    contribuyentes.append(contribuyente)

    # Guardar de nuevo en el archivo JSON
    with open("contribuyentes.json", "w") as file:
        json.dump(contribuyentes, file)

def cargar_contribuyentes():
    try:
        with open("contribuyentes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []