import tkinter as tk
from tkinter import messagebox
from informes import generar_informe
from json_manager import guardar_contribuyente
from utils import validar_edad


def iniciar_gui():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")

    def abrir_registro():
        ventana_principal.withdraw()
        registrar_contribuyente()

    def generar_informes():
        generar_informe()
        messagebox.showinfo(
            "Informe", "El informe ha sido generado y se muestra en la terminal."
        )

    def salir():
        ventana_principal.quit()

    btn_registrar = tk.Button(
        ventana_principal, text="Ingresar Contribuyente", command=abrir_registro
    )
    btn_registrar.pack(pady=10)

    btn_informe = tk.Button(
        ventana_principal, text="Generar Informe", command=generar_informes
    )
    btn_informe.pack(pady=10)

    btn_salir = tk.Button(ventana_principal, text="Salir", command=salir)
    btn_salir.pack(pady=10)

    ventana_principal.mainloop()


def registrar_contribuyente():
    ventana_registro = tk.Tk()
    ventana_registro.title("Registrar Contribuyente")

    # Creación de los widgets Entry
    tk.Label(ventana_registro, text="DNI:").pack()
    dni_entry = tk.Entry(ventana_registro)
    dni_entry.pack()

    tk.Label(ventana_registro, text="Nombre:").pack()
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack()

    tk.Label(ventana_registro, text="Apellido:").pack()
    apellido_entry = tk.Entry(ventana_registro)
    apellido_entry.pack()

    tk.Label(ventana_registro, text="Edad:").pack()
    edad_entry = tk.Entry(ventana_registro)
    edad_entry.pack()

    tk.Label(ventana_registro, text="Fecha (DD/MM/AAAA):").pack()
    fecha_entry = tk.Entry(ventana_registro)
    fecha_entry.pack()

    tk.Label(ventana_registro, text="Monto:").pack()
    monto_entry = tk.Entry(ventana_registro)
    monto_entry.pack()

    tk.Label(ventana_registro, text="Origen de los fondos:").pack()
    origen_entry = tk.Entry(ventana_registro)
    origen_entry.pack()

    def guardar():
        try:
            # Obtener valores directamente de los widgets Entry
            dni = dni_entry.get().strip()
            nombre = nombre_entry.get().strip()
            apellido = apellido_entry.get().strip()
            edad = edad_entry.get().strip()
            fecha = fecha_entry.get().strip()
            monto = monto_entry.get().strip()
            origen = origen_entry.get().strip()

            # Imprimir valores de depuración
            print(f"DNI: '{dni}'")
            print(f"Nombre: '{nombre}'")
            print(f"Apellido: '{apellido}'")
            print(f"Edad: '{edad}'")
            print(f"Fecha: '{fecha}'")
            print(f"Monto: '{monto}'")
            print(f"Origen: '{origen}'")

            # Validaciones
            if not dni:
                raise ValueError("El DNI no puede estar vacío.")
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            if not apellido:
                raise ValueError("El apellido no puede estar vacío.")
            if not edad or not validar_edad(edad):
                raise ValueError("La edad debe ser un número entero válido.")
            if not fecha:
                raise ValueError("La fecha no puede estar vacía.")
            if not monto:
                raise ValueError("El monto no puede estar vacío.")
            try:
                monto = float(monto)
            except ValueError:
                raise ValueError("El monto debe ser un número válido.")
            if not origen:
                raise ValueError("El origen de los fondos no puede estar vacío.")

            contribuyente = {
                "dni": dni,
                "nombre": nombre,
                "apellido": apellido,
                "edad": int(edad),
                "fecha": fecha,
                "monto": monto,
                "origen": origen,
            }

            guardar_contribuyente(contribuyente)
            messagebox.showinfo("Éxito", "Contribuyente guardado correctamente.")
            ventana_registro.destroy()

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    # Botón para guardar contribuyente
    btn_guardar = tk.Button(ventana_registro, text="Guardar", command=guardar)
    btn_guardar.pack(pady=10)

    ventana_registro.mainloop()