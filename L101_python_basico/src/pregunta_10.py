
import gzip
import os.path
import csv

def pregunta_10():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    resultado = []

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
       

        for columnas in lector:
            letra = columnas[0]
            codigos = columnas[3].split(",")
            metricas = columnas[4].split(",")

            cantidad_codigos = len(codigos)
            cantidad_metricas = len(metricas)

            resultado.append((letra, cantidad_codigos, cantidad_metricas))

    return resultado
