import json
from datetime import datetime
from utils import cargar_contribuyentes

# Función para generar los informes
def generar_informe():
    contribuyentes = cargar_contribuyentes()
    
    if not contribuyentes:
        return None  # Devolver None si no hay contribuyentes

    # Calcular cantidad de registros
    cantidad = len(contribuyentes)

    # Obtener lista de edades
    edades = [contribuyente["edad"] for contribuyente in contribuyentes]
    
    # Obtener la edad mínima, máxima y el promedio
    edad_minima = min(edades)
    edad_maxima = max(edades)
    edad_promedio = sum(edades) / len(edades)

    # Obtener lista de fechas en formato datetime, ignorando fechas no válidas
    fechas = []
    for contribuyente in contribuyentes:
        try:
            fecha = datetime.strptime(contribuyente["fecha"], "%d/%m/%Y")
            fechas.append(fecha)
        except ValueError:
            print(f"Fecha no válida para el contribuyente {contribuyente['nombre']}: {contribuyente['fecha']}")

    # Verificamos si hay fechas válidas antes de continuar
    if fechas:
        fecha_mas_cercana = min(fechas).strftime("%d/%m/%Y")
        fecha_mas_lejana = max(fechas).strftime("%d/%m/%Y")
    else:
        fecha_mas_cercana = "N/A"
        fecha_mas_lejana = "N/A"

    # Crear una cadena de texto con el informe
    informe_texto = (
        f"Cantidad de contribuyentes registrados: {cantidad}\n"
        f"Edad mínima: {edad_minima}\n"
        f"Edad máxima: {edad_maxima}\n"
        f"Edad promedio: {edad_promedio:.2f}\n"
        f"Fecha de declaración más cercana: {fecha_mas_cercana}\n"
        f"Fecha de declaración más lejana: {fecha_mas_lejana}\n"
    )

    return informe_texto  # Devolver el informe como cadena de texto