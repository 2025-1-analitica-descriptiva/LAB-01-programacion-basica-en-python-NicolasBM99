"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    months={}
    with open("C:/Users/nicoo/Documents/GitHub/LAB-01-programacion-basica-en-python-NicolasBM99/files/input/data.csv", encoding="utf-8")  as csvfile:
        for row in csvfile:
            colum = row.split("\t")
            if len(colum) >= 3:
                date = colum[2]
                month = date.split("-")[1]  # YYYY-MM-DD → [YYYY, MM, DD]
                months[month] = months.get(month, 0) + 1

    return sorted(months.items())

if __name__ == "__main__":
    print(pregunta_04())