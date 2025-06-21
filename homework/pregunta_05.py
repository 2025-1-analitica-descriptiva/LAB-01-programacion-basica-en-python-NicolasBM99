"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    data = {}
    with open("C:/Users/nicoo/Documents/GitHub/LAB-01-programacion-basica-en-python-NicolasBM99/files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.strip().split("\t")
            if len(colum) >= 2:
                letter = colum[0]
                try:
                    num = int(colum[1])
                    if letter not in data:
                        data[letter] = []
                    data[letter].append(num)
                except ValueError:
                    pass

    answer = []
    for letter in sorted(data.keys()):
        max1 = max(data[letter])
        min1 = min(data[letter])
        answer.append((letter, max1, min1))
    return answer

if __name__ == "__main__":
    print(pregunta_05())