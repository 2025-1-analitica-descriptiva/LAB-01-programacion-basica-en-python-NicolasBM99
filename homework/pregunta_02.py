"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    count = {}
    with open("files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.split("\t")
            if len(colum) >= 1:
                #print(count[letter])
                letter = colum[0]
                count[letter] = count.get(letter, 0) + 1
    answer = sorted(count.items())
    return answer

#if __name__ == "__main__":
#    print(pregunta_02())