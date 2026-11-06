
import gzip
import os.path
import csv

def pregunta_12():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    sumas = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
     

        for columnas in lector:
            letra = columnas[0]
            metricas = columnas[4].split(",")

            for metrica in metricas:
                datos = metrica.split(":")
                valor = int(datos[1])

                if letra in sumas:
                    sumas[letra] = sumas[letra] + valor
                else:
                    sumas[letra] = valor

    resultado = {}

    for letra in sorted(sumas):
        resultado[letra] = sumas[letra]

    return resultado
