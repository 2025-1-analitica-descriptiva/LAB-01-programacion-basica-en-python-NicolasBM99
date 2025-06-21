"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    result = []

    with open("files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.strip().split("\t")
            letter = colum[0]
            col4 = colum[3].split(",")
            col5 = colum[4].split(",")
            result.append((letter, len(col4), len(col5)))

    return result
