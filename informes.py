from datetime import datetime
from utils import cargar_contribuyentes

def generar_informe():
    contribuyentes = cargar_contribuyentes()
    
    if not contribuyentes:
        print("No hay contribuyentes registrados.")
        return

    cantidad = len(contribuyentes)
    edades = [contribuyente["edad"] for contribuyente in contribuyentes]
    edad_minima = min(edades)
    edad_maxima = max(edades)
    edad_promedio = sum(edades) / len(edades)

    fechas = []
    for contribuyente in contribuyentes:
        try:
            fecha = datetime.strptime(contribuyente["fecha"], "%d/%m/%Y")
            fechas.append(fecha)
        except ValueError:
            print(f"Fecha no válida para {contribuyente['nombre']}: {contribuyente['fecha']}")

    if fechas:
        fecha_mas_cercana = min(fechas).strftime("%d/%m/%Y")
        fecha_mas_lejana = max(fechas).strftime("%d/%m/%Y")
    else:
        fecha_mas_cercana = "N/A"
        fecha_mas_lejana = "N/A"

    print(f"Cantidad de contribuyentes registrados: {cantidad}")
    print(f"Edad mínima: {edad_minima}")
    print(f"Edad máxima: {edad_maxima}")
    print(f"Edad promedio: {edad_promedio:.2f}")
    print(f"Fecha de declaración más cercana: {fecha_mas_cercana}")
    print(f"Fecha de declaración más lejana: {fecha_mas_lejana}")