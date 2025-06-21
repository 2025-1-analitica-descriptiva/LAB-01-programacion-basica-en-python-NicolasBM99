"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    value_key = {}

    with open("C:/Users/nicoo/Documents/GitHub/LAB-01-programacion-basica-en-python-NicolasBM99/files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.strip().split("\t")
            if len(colum) >= 5:
                pars = colum[4].split(",")
                for par in pars:
                    if ":" in par:
                        key, value = par.split(":")
                        try:
                            value = int(value)
                            if key not in value_key:
                                value_key[key] = []
                            value_key[key].append(value)
                        except ValueError:
                            pass

    answer = []
    for key in sorted(value_key.keys()):
        vmin = min(value_key[key])
        vmax = max(value_key[key])
        answer.append((key, vmin, vmax))

    return answer

if __name__ == "__main__":
    print(pregunta_06())