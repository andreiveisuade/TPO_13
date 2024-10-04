import tkinter as tk
from tkinter import messagebox
from utils import validar_contribuyente
from json_manager import guardar_contribuyente

def registrar_contribuyente(ventana_principal):
    # Ocultar la ventana principal
    ventana_principal.withdraw()

    ventana_registro = tk.Toplevel()  # Creamos una nueva ventana
    ventana_registro.title("Registrar Contribuyente")

    # Función para volver al menú principal
    def volver_al_menu():
        ventana_registro.destroy()  # Cerramos la ventana de registro
        ventana_principal.deiconify()  # Mostramos la ventana principal nuevamente

    # Creación de los campos de entrada
    entries = {}
    labels = {
        "dni": "DNI",
        "nombre": "Nombre",
        "apellido": "Apellido",
        "edad": "Edad",
        "fecha": "Fecha (DD/MM/AAAA)",  # Asignamos explícitamente la clave "fecha"
        "monto": "Monto",
        "origen": "Origen de los fondos"
    }

    for key, label in labels.items():
        tk.Label(ventana_registro, text=label + ":").pack()
        entry = tk.Entry(ventana_registro)
        entry.pack()
        entries[key] = entry  # Guardamos la clave correcta

    def guardar():
        # Recopilar datos
        contribuyente = {key: entry.get().strip() for key, entry in entries.items()}
        contribuyente["edad"] = int(contribuyente["edad"])
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

    # Botón para guardar contribuyente
    btn_guardar = tk.Button(ventana_registro, text="Guardar", command=guardar)
    btn_guardar.pack(pady=10)

    # Botón para volver al menú principal
    btn_volver = tk.Button(ventana_registro, text="Volver al Menú", command=volver_al_menu)
    btn_volver.pack(pady=10)

    ventana_registro.mainloop()