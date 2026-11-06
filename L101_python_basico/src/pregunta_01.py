
import gzip
import os.path

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (value)
    del archivo data/data.csv.gz y retorne un número entero.
    """

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    suma = 0

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        

        for linea in archivo:
            columnas = linea.strip().split("\t")
            valor = int(columnas[1])
            suma = suma + valor

    return suma
