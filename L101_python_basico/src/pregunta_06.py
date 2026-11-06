
import gzip
import os.path
import csv

def pregunta_06():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    valores = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        

        lector = csv.reader(archivo, delimiter="\t")

        for columnas in lector:
            metricas = columnas[4].split(",")

            for metrica in metricas:
                datos = metrica.split(":")
                clave = datos[0]
                valor = int(datos[1])

                if clave in valores:
                    if valor < valores[clave][0]:
                        valores[clave][0] = valor

                    if valor > valores[clave][1]:
                        valores[clave][1] = valor
                else:
                    valores[clave] = [valor, valor]

    resultado = []

    for clave in sorted(valores):
        resultado.append((clave, valores[clave][0], valores[clave][1]))

    return resultado
