
import gzip
import os.path

def pregunta_05():
    """
    Para cada letra de la primera columna (letter), encuentre
    el valor máximo y el valor mínimo de la segunda columna (value).
    """

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    valores = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
        

        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if letra in valores:
                if valor > valores[letra][0]:
                    valores[letra][0] = valor

                if valor < valores[letra][1]:
                    valores[letra][1] = valor
            else:
                valores[letra] = [valor, valor]

    resultado = []

    for letra in sorted(valores):
        resultado.append((letra, valores[letra][0], valores[letra][1]))

    return resultado

