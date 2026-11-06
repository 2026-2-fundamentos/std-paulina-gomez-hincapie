
import gzip
import os.path
import csv

def pregunta_09():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    conteo = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
  

        for columnas in lector:
            metricas = columnas[4].split(",")

            for metrica in metricas:
                datos = metrica.split(":")
                clave = datos[0]

                if clave in conteo:
                    conteo[clave] = conteo[clave] + 1
                else:
                    conteo[clave] = 1

    resultado = {}

    for clave in sorted(conteo):
        resultado[clave] = conteo[clave]

    return resultado

