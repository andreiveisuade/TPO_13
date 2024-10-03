from json_manager import cargar_contribuyentes
from informes import generar_informes

def mostrar_informes():
    # Cargar los contribuyentes desde el archivo JSON
    contribuyentes = cargar_contribuyentes()

    if contribuyentes:
        informes = generar_informes(contribuyentes)
        print("\nInforme Estadístico:")
        print(f"Cantidad de registros: {informes['cantidad']}")
        print(f"Edad mínima: {informes['edad_minima']}")
        print(f"Edad máxima: {informes['edad_maxima']}")
        print(f"Edad promedio: {informes['edad_promedio']:.2f}")
        print(f"Fecha de declaración más lejana: {informes['fecha_mas_lejana']}")
        print(f"Fecha de declaración más cercana: {informes['fecha_mas_cercana']}")
    else:
        print("No hay contribuyentes registrados aún.")

if __name__ == "__main__":
    mostrar_informes()