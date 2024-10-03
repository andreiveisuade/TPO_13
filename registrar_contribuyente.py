import tkinter as tk
from tkinter import messagebox
from json_manager import guardar_contribuyente
from utils import validar_edad, validar_dni, validar_fecha, validar_monto

def registrar_contribuyente():
    ventana_registro = tk.Tk()
    ventana_registro.title("Registrar Contribuyente")

    # Creación de los widgets Entry
    entries = []
    for label in ["DNI:", "Nombre:", "Apellido:", "Edad:", "Fecha (DD/MM/AAAA):", "Monto:", "Origen de los fondos:"]:
        tk.Label(ventana_registro, text=label).pack()
        entry = tk.Entry(ventana_registro)
        entry.pack()
        entries.append(entry)

    def guardar():
        try:
            contribuyente = {}
            for entry, label in zip(entries, ["dni", "nombre", "apellido", "edad", "fecha", "monto", "origen"]):
                valor = entry.get().strip()
                if label == "edad":
                    valor = int(valor)  # Convierte a entero
                elif label == "monto":
                    valor = float(valor)  # Convierte a float
                contribuyente[label] = valor

            # Validaciones
            print("Datos a validar:", contribuyente)  # Mensaje de depuración

            if not validar_dni(str(contribuyente["dni"])):
                print("DNI inválido.")
            if not contribuyente["nombre"]:
                print("Nombre inválido.")
            if not contribuyente["apellido"]:
                print("Apellido inválido.")
            if not validar_edad(contribuyente["edad"]):
                print("Edad inválida.")
            if not validar_fecha(contribuyente["fecha"]):
                print("Fecha inválida.")
            if not validar_monto(contribuyente["monto"]):
                print("Monto inválido.")
            
            if not (
                validar_dni(str(contribuyente["dni"])) and 
                contribuyente["nombre"] and 
                contribuyente["apellido"] and 
                validar_edad(contribuyente["edad"]) and 
                validar_fecha(contribuyente["fecha"]) and 
                validar_monto(contribuyente["monto"]) and 
                contribuyente["origen"]
            ):
                raise ValueError("Datos inválidos.")

            guardar_contribuyente(contribuyente)
            messagebox.showinfo("Éxito", "Contribuyente guardado correctamente.")

            # Limpiar los campos
            for entry in entries:
                entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    # Botón para guardar contribuyente
    btn_guardar = tk.Button(ventana_registro, text="Guardar", command=guardar)
    btn_guardar.pack(pady=10)

    ventana_registro.mainloop()