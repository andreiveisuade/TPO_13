from datetime import datetime
from statistics import mean
from utils import cargar_contribuyentes, validar_fecha

# Función para generar los informes
def generar_informe():
    contribuyentes = cargar_contribuyentes()
    
    if not contribuyentes:
        return None  # Devolver None si no hay contribuyentes

    # Obtener listas de edades y fechas válidas
    edades = []
    fechas = []
    for contribuyente in contribuyentes:
        # Validar y almacenar la edad
        if "edad" in contribuyente and isinstance(contribuyente["edad"], int):
            edades.append(contribuyente["edad"])
        
        # Validar y almacenar la fecha
        fecha = contribuyente.get("fecha")
        if validar_fecha(fecha):
            fechas.append(datetime.strptime(fecha, "%d/%m/%Y"))
        else:
            print(f"Fecha no válida para el contribuyente {contribuyente['nombre']}: {fecha}")

    # Calcular estadísticas de edad
    if edades:
        edad_minima = min(edades)
        edad_maxima = max(edades)
        edad_promedio = mean(edades)
    else:
        edad_minima = edad_maxima = edad_promedio = "N/A"

    # Obtener fechas más cercanas y lejanos
    if fechas:
        fecha_mas_cercana = min(fechas).strftime("%d/%m/%Y")
        fecha_mas_lejana = max(fechas).strftime("%d/%m/%Y")
    else:
        fecha_mas_cercana = fecha_mas_lejana = "N/A"

    # Crear una cadena de texto con el informe
    informe_texto = (
        f"Cantidad de contribuyentes registrados: {len(contribuyentes)}\n"
        f"Edad mínima: {edad_minima}\n"
        f"Edad máxima: {edad_maxima}\n"
        f"Edad promedio: {edad_promedio:.2f}\n"
        f"Fecha de declaración más cercana: {fecha_mas_cercana}\n"
        f"Fecha de declaración más lejana: {fecha_mas_lejana}\n"
    )

    return informe_texto  # Devolver el informe como cadena de texto