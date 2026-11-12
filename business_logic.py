from datetime import date, timedelta
from math import sqrt
from random import randint

# Diccionario que guarda todos los museos.
museos = {}


def convertir_entero(valor):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return None


# Requisito 1: crear un museo.
def crear_museo(nombre, aforo, anio, mes, dia):
    nombre = nombre.strip()

    if nombre == "":
        return "Error: el nombre no puede estar vacío."
    if nombre in museos:
        return "Error: ya existe un museo con ese nombre."

    aforo = convertir_entero(aforo)
    if aforo is None:
        return "Error: el aforo diario debe ser un número entero."
    if aforo < 1:
        return "Error: el aforo diario debe ser de al menos un visitante."

    anio = convertir_entero(anio)
    mes = convertir_entero(mes)
    dia = convertir_entero(dia)
    if anio is None or mes is None or dia is None:
        return "Error: la fecha no es válida."

    try:
        fecha_inicio = date(anio, mes, dia)
    except ValueError:
        return "Error: la fecha no es válida."

    museos[nombre] = {
        "nombre": nombre,
        "aforo": aforo,
        "fecha_inicio": fecha_inicio,
        "dias": []
    }
    return "Museo creado correctamente."


def buscar_museo(nombre):
    return museos.get(nombre.strip())


def fecha_siguiente(museo):
    return museo["fecha_inicio"] + timedelta(days=len(museo["dias"]))


# Requisito 2: registrar visitantes del siguiente día.
def registrar_visitantes(nombre, visitantes):
    museo = buscar_museo(nombre)
    if museo is None:
        return "Error: no hay un museo con ese nombre."

    visitantes = convertir_entero(visitantes)
    if visitantes is None:
        return "Error: los visitantes deben ser un número entero."
    if visitantes < 0 or visitantes > museo["aforo"]:
        return "Error: los visitantes van de 0 a " + str(museo["aforo"]) + "."

    fecha = fecha_siguiente(museo)
    museo["dias"].append({"fecha": fecha, "visitantes": visitantes})
    return "Visitantes registrados para el " + str(fecha) + "."


# Requisito 3: simular días.
def simular_dias(nombre, cantidad, minimo, maximo):
    museo = buscar_museo(nombre)
    if museo is None:
        return "Error: no hay un museo con ese nombre."

    cantidad = convertir_entero(cantidad)
    if cantidad is None:
        return "Error: el número de días debe ser un número entero."
    if cantidad < 1:
        return "Error: se debe simular al menos un día."

    minimo = convertir_entero(minimo)
    maximo = convertir_entero(maximo)
    if minimo is None or maximo is None:
        return "Error: los visitantes deben ser un número entero."
    if minimo < 0 or minimo > museo["aforo"]:
        return "Error: los visitantes van de 0 a " + str(museo["aforo"]) + "."
    if maximo < 0 or maximo > museo["aforo"]:
        return "Error: los visitantes van de 0 a " + str(museo["aforo"]) + "."
    if minimo > maximo:
        return "Error: el mínimo no puede ser mayor que el máximo."

    for i in range(cantidad):
        fecha = fecha_siguiente(museo)
        visitantes = randint(minimo, maximo)
        museo["dias"].append({"fecha": fecha, "visitantes": visitantes})

    return str(cantidad) + " días simulados correctamente."


# Requisitos 4 y 5: informe y desviación estándar.
def informe_museo(nombre):
    museo = buscar_museo(nombre)
    if museo is None:
        return "Error: no hay un museo con ese nombre."

    resultado = "Museo: " + museo["nombre"] + "\n"
    resultado += "Aforo diario: " + str(museo["aforo"]) + "\n"

    cantidad = len(museo["dias"])
    if cantidad == 0:
        return resultado + "No tiene días registrados."

    total = 0
    for dia in museo["dias"]:
        total += dia["visitantes"]

    promedio_sin_redondear = total / cantidad
    porcentaje = round(promedio_sin_redondear / museo["aforo"] * 100, 2)

    suma_cuadrados = 0
    for dia in museo["dias"]:
        diferencia = dia["visitantes"] - promedio_sin_redondear
        suma_cuadrados += diferencia ** 2

    desviacion = round(sqrt(suma_cuadrados / cantidad), 2)

    resultado += "Días registrados: " + str(cantidad) + "\n"
    resultado += "Visitantes totales: " + str(total) + "\n"
    resultado += "Promedio diario: " + str(round(promedio_sin_redondear, 2)) + "\n"
    resultado += "Porcentaje de asistencia: " + str(porcentaje) + " %\n"
    resultado += "Desviación estándar: " + str(desviacion)
    return resultado
