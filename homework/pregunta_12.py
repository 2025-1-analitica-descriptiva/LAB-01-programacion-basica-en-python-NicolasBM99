"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sum_per_letter = {}

    with open("C:/Users/nicoo/Documents/GitHub/LAB-01-programacion-basica-en-python-NicolasBM99/files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.strip().split("\t")
            letter = colum[0]
            pars = colum[4].split(",")
            sum_values = 0
            for par in pars:
                key, value = par.split(":")
                sum_values += int(value)
            sum_per_letter[letter] = sum_per_letter.get(letter, 0) + sum_values

    return dict(sorted(sum_per_letter.items()))