
from datetime import date

museos = {}


def crear_museo(nombre, aforo, anio, mes, dia):
    if not nombre.strip():
        return "Error: el nombre no puede estar vacío."

    if nombre in museos:
        return "Error: el museo ya existe."

    if type(aforo) is not int:
        return "Error: el aforo debe ser un entero."

    if aforo < 1:
        return "Error: el aforo debe ser mayor o igual a 1."

    try:
        fecha_inicio = date(anio, mes, dia)
    except (ValueError, TypeError):
        return "Error: la fecha no es válida."

    museos[nombre] = {
        "nombre": nombre,
        "aforo": aforo,
        "fecha_inicio": fecha_inicio,
        "dias": []
    }

    return "Museo creado correctamente."
