
import gzip
import os.path

def pregunta_02():
    """
    Cuente cuántos registros hay para cada letra de la primera columna
    (`letter`). Retorne una lista de tuplas (letra, cantidad) ordenada
    alfabéticamente por la letra.
    """

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    conteo = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        

        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]

            if letra in conteo:
                conteo[letra] = conteo[letra] + 1
            else:
                conteo[letra] = 1

    resultado = []

    for letra in sorted(conteo):
        resultado.append((letra, conteo[letra]))

    return resultado

