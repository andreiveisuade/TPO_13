import tkinter as tk
from tkinter import messagebox
from informes import generar_informe
from registrar_contribuyente import registrar_contribuyente

def iniciar_gui():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("300x150")

    tk.Button(ventana_principal, text="Ingresar Contribuyente", command=lambda: registrar_contribuyente(ventana_principal)).pack(pady=10)
    tk.Button(ventana_principal, text="Generar Informe", command=lambda: (generar_informe(), messagebox.showinfo("Informe", "El informe ha sido generado y se muestra en la terminal."))).pack(pady=10)
    tk.Button(ventana_principal, text="Salir", command=ventana_principal.quit).pack(pady=10)

    ventana_principal.mainloop()
