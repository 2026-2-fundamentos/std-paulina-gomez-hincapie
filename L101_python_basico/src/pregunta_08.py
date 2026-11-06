
import gzip
import os.path

def pregunta_08():

    carpeta = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(carpeta, "data", "data.csv.gz")

    valores = {}

    with gzip.open(ruta, "rt", encoding="utf-8") as archivo:
      

        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if valor in valores:
                if letra not in valores[valor]:
                    valores[valor].append(letra)
            else:
                valores[valor] = [letra]

    resultado = []

    for valor in sorted(valores):
        letras = sorted(valores[valor])
        resultado.append((valor, letras))

    return resultado
