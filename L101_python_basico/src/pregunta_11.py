
import gzip
import os.path
import csv

def pregunta_11():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    sumas = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
       
        for columnas in lector:
            valor = int(columnas[1])
            codigos = columnas[3].split(",")

            for letra in codigos:
                if letra in sumas:
                    sumas[letra] = sumas[letra] + valor
                else:
                    sumas[letra] = valor

    resultado = {}

    for letra in sorted(sumas):
        resultado[letra] = sumas[letra]

    return resultado

