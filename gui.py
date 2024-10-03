import tkinter as tk
from tkinter import messagebox
from informes import generar_informe
from json_manager import guardar_contribuyente
from utils import validar_edad, validar_dni, validar_fecha, validar_monto
from registrar_contribuyente import registrar_contribuyente  # Importar la función

def iniciar_gui():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")

    def abrir_registro():
        ventana_principal.withdraw()
        registrar_contribuyente()  # Llamar a la función de otro archivo

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