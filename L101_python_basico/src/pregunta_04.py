
import gzip
import os.path

def pregunta_04():
    """
    Cuente cuántos registros hay en cada mes, usando la fecha
    de la tercera columna (date).
    """

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    conteo = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
       

        for linea in archivo:
            columnas = linea.strip().split("\t")
            fecha = columnas[2]
            mes = fecha.split("-")[1]

            if mes in conteo:
                conteo[mes] = conteo[mes] + 1
            else:
                conteo[mes] = 1

    resultado = []

    for mes in sorted(conteo):
        resultado.append((mes, conteo[mes]))

    return resultado
