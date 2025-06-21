"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """



    suma_total = 0
    with open("files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            row = row.strip()
            colum = row.split("\t")
            #print(row)
            if len(colum) >= 2:
                try:
                    suma_total += int(colum[1])
                except (IndexError, ValueError):
                    pass 
    return suma_total

#if __name__ == "__main__":
#    print(pregunta_01())