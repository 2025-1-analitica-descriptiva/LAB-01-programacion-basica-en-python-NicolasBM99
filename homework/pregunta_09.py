"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    count = {}
    with open("C:/Users/nicoo/Documents/GitHub/LAB-01-programacion-basica-en-python-NicolasBM99/files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.strip().split("\t")
            if len(colum) >= 5:
                pars = colum[4].split(",")
                for par in pars:
                    key, _ = par.split(":")
                    count[key] = count.get(key, 0) + 1

    return dict(sorted(count.items()))