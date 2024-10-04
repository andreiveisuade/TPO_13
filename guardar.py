import json
import tkinter as tk
from tkinter import messagebox
from utils import validar_contribuyente

# Definir la función guardar_contribuyente dentro de este archivo
def guardar_contribuyente(contribuyente):
    try:
        # Abrir el archivo JSON de contribuyentes o crearlo si no existe
        with open("contribuyentes.json", "r") as file:
            contribuyentes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contribuyentes = []

    # Agregar el nuevo contribuyente a la lista
    contribuyentes.append(contribuyente)

    # Guardar la lista actualizada en el archivo JSON
    with open("contribuyentes.json", "w") as file:
        json.dump(contribuyentes, file, indent=4)

    print("Contribuyente guardado exitosamente")

def guardar(entries):
    # Recopilar datos
    contribuyente = {key: entry.get().strip() for key, entry in entries.items()}
    try:
        contribuyente["edad"] = int(contribuyente["edad"])
    except ValueError:
        messagebox.showerror("Error de validación", "La edad debe ser un número entero.")
        return
    contribuyente["monto"] = float(contribuyente["monto"])

    # Validar datos
    errores = validar_contribuyente(contribuyente)
    if errores:
        messagebox.showerror("Error de validación", "\n".join(errores))
        return

    # Guardar contribuyente
    guardar_contribuyente(contribuyente)
    messagebox.showinfo("Éxito", "Contribuyente guardado correctamente.")

    # Limpiar campos
    for entry in entries.values():
        entry.delete(0, tk.END)