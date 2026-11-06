
import gzip
import os.path

def pregunta_03():
    """
    Sume los valores de la segunda columna (value) para cada letra
    de la primera columna (letter).
    """

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    sumas = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        

        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if letra in sumas:
                sumas[letra] = sumas[letra] + valor
            else:
                sumas[letra] = valor

    resultado = []

    for letra in sorted(sumas):
        resultado.append((letra, sumas[letra]))

    return resultado
