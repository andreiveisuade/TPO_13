import tkinter as tk
from tkinter import messagebox, scrolledtext
from generar_informes import generar_informe
from registrar_contribuyente import registrar_contribuyente

def iniciar_gui():
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")

    def abrir_registro():
        registrar_contribuyente(ventana_principal)

    def generar_informes():
        ventana_informe = tk.Toplevel(ventana_principal)
        ventana_informe.title("Informe")

        text_area = scrolledtext.ScrolledText(ventana_informe, width=60, height=20)
        text_area.pack(pady=10)

        informes = generar_informe()
        if informes:
            text_area.insert(tk.END, informes)  
        else:
            messagebox.showinfo("Informe", "No hay contribuyentes registrados.")

        btn_salir = tk.Button(ventana_informe, text="Salir", command=ventana_informe.destroy)
        btn_salir.pack(pady=10)

    def salir():
        ventana_principal.quit()

    btn_registrar = tk.Button(ventana_principal, text="Ingresar Contribuyente", command=abrir_registro)
    btn_registrar.pack(pady=10)

    btn_informe = tk.Button(ventana_principal, text="Generar Informe", command=generar_informes)
    btn_informe.pack(pady=10)

    btn_salir = tk.Button(ventana_principal, text="Salir", command=salir)
    btn_salir.pack(pady=10)

    ventana_principal.mainloop()