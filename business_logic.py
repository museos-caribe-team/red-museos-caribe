import os
import re
from datetime import date, timedelta
from fractions import Fraction
from random import randint


# Auxiliar (Requisitos 12 y 13): ¿el texto es un número entero?
def es_entero(texto: str) -> bool:
    return re.fullmatch(r"[+-]?[0-9]+", texto.strip()) is not None


# Auxiliar (Requisito 12): crear una fecha o devolver None si no es válida
def crear_fecha(anio: str, mes: str, dia: str) -> date | None:
    if not (es_entero(anio) and es_entero(mes) and es_entero(dia)):
        return None
    try:
        return date(int(anio), int(mes), int(dia))
    except ValueError:
        return None


class Museo:

    def __init__(self, nombre: str, aforo: int, fecha_inicio: date):
        self.nombre = nombre
        self.aforo = aforo
        self.fecha_inicio = fecha_inicio
        self.visitantes = []

    # Requisito 2: calcular la fecha del siguiente registro
    def calcular_fecha_siguiente(self):
        cantidad_dias = len(self.visitantes)
        fecha = self.fecha_inicio + timedelta(days=cantidad_dias)
        return fecha

    # Requisito 2: registrar los visitantes del día siguiente
    def registrar_visitantes(self, cantidad: int):
        if type(cantidad) is not int:
            raise ValueError("Los visitantes deben ser un número entero")
        if cantidad < 0 or cantidad > self.aforo:
            raise ValueError(f"Los visitantes deben estar entre 0 y {self.aforo}")
        fecha = self.calcular_fecha_siguiente()
        self.visitantes.append(cantidad)
        return fecha

    # Requisito 3: simular días
    def simular_dias(self, dias: int, minimo: int, maximo: int):
        if type(dias) is not int or dias < 1:
            raise ValueError("La cantidad de días debe ser un entero mayor o igual a 1")
        if type(minimo) is not int or minimo < 0 or minimo > self.aforo:
            raise ValueError(f"El mínimo debe ser un entero entre 0 y {self.aforo}")
        if type(maximo) is not int or maximo < 0 or maximo > self.aforo:
            raise ValueError(f"El máximo debe ser un entero entre 0 y {self.aforo}")
        if minimo > maximo:
            raise ValueError("El mínimo no puede ser mayor que el máximo")
        for i in range(dias):
            cantidad = randint(minimo, maximo)
            self.registrar_visitantes(cantidad)

    # Requisito 4: calcular el total de visitantes
    def calcular_total(self) -> int:
        total = 0
        for cantidad in self.visitantes:
            total = total + cantidad
        return total

    # Requisito 4: calcular el promedio diario
    def calcular_promedio(self) -> float:
        cantidad_dias = len(self.visitantes)
        if cantidad_dias == 0:
            return 0.0
        return self.calcular_total() / cantidad_dias

    # Requisito 4: calcular el porcentaje de asistencia
    def calcular_porcentaje(self) -> float:
        porcentaje = self.calcular_promedio() / self.aforo * 100
        return round(porcentaje, 2)

    # Requisito 11: porcentaje de asistencia sin redondear (fracción exacta,
    # para que dos museos con el mismo porcentaje empaten de verdad)
    def calcular_porcentaje_exacto(self) -> Fraction:
        return Fraction(self.calcular_total() * 100, len(self.visitantes) * self.aforo)

    # Requisito 5: calcular la desviación estándar poblacional
    def calcular_desviacion(self) -> float:
        cantidad_dias = len(self.visitantes)
        if cantidad_dias == 0:
            return 0.0
        promedio = self.calcular_promedio()
        suma_cuadrados = 0
        for cantidad in self.visitantes:
            diferencia = cantidad - promedio
            suma_cuadrados = suma_cuadrados + diferencia ** 2
        varianza = suma_cuadrados / cantidad_dias
        desviacion = varianza ** 0.5
        return round(desviacion, 2)
        
    # Requisito 6: fecha del día con más visitantes (primera aparición en empate)
    def encontrar_dia_mas_visitantes(self) -> date | None:
        if len(self.visitantes) == 0:
            return None
        indice_max = 0
        for i in range(1, len(self.visitantes)):
            if self.visitantes[i] > self.visitantes[indice_max]:
                indice_max = i
        return self.fecha_inicio + timedelta(days=indice_max)

    # Requisito 6: fecha del día con menos visitantes (primera aparición en empate)
    def encontrar_dia_menos_visitantes(self) -> date | None:
        if len(self.visitantes) == 0:
            return None
        indice_min = 0
        for i in range(1, len(self.visitantes)):
            if self.visitantes[i] < self.visitantes[indice_min]:
                indice_min = i
        return self.fecha_inicio + timedelta(days=indice_min)

    # Método interno auxiliar (Requisitos 7 y 8): clasificar el nivel de un día
    def clasificar_nivel_dia(self, cantidad: int) -> str:
        porcentaje_dia = (cantidad / self.aforo) * 100
        if porcentaje_dia < 30:
            return "Baja"
        elif porcentaje_dia < 60:
            return "Media"
        elif porcentaje_dia < 85:
            return "Alta"
        else:
            return "Plena"

    # Requisito 7: contar días en cada nivel de asistencia (baja, media, alta, plena)
    def contar_dias_por_nivel(self) -> tuple[int, int, int, int]:
        baja = 0
        media = 0
        alta = 0
        plena = 0
        for cantidad in self.visitantes:
            nivel = self.clasificar_nivel_dia(cantidad)
            if nivel == "Baja":
                baja = baja + 1
            elif nivel == "Media":
                media = media + 1
            elif nivel == "Alta":
                alta = alta + 1
            else:
                plena = plena + 1
        return baja, media, alta, plena

    # Requisito 8: racha más larga en asistencia baja (longitud y fecha de inicio)
    def encontrar_racha_baja_mas_larga(self) -> tuple[int, date | None]:
        racha_actual = 0
        racha_maxima = 0
        inicio_actual = None
        inicio_maxima = None

        for i in range(len(self.visitantes)):
            if self.clasificar_nivel_dia(self.visitantes[i]) == "Baja":
                if racha_actual == 0:
                    inicio_actual = self.fecha_inicio + timedelta(days=i)
                racha_actual = racha_actual + 1
                if racha_actual > racha_maxima:
                    racha_maxima = racha_actual
                    inicio_maxima = inicio_actual
            else:
                racha_actual = 0

        return racha_maxima, inicio_maxima

    # Requisito 9: fecha del último día registrado
    def obtener_ultimo_dia_registrado(self) -> date | None:
        cantidad_dias = len(self.visitantes)
        if cantidad_dias == 0:
            return None
        return self.fecha_inicio + timedelta(days=cantidad_dias - 1)

    # Requisito 9: días pendientes por registrar hasta ayer
    def calcular_dias_sin_registrar(self, fecha_actual: date) -> int:
        ultimo_dia = self.obtener_ultimo_dia_registrado()
        if ultimo_dia is None:
            return 0
        ayer = fecha_actual - timedelta(days=1)
        if ultimo_dia >= ayer:
            return 0
        return (ayer - ultimo_dia).days

class RedMuseos:

    def __init__(self):
        self.museos = []

    # Requisito 10: buscar museo ignorando espacios laterales y respetando mayúsculas y tildes
    def buscar_museo(self, nombre: str) -> Museo | None:
        nombre_limpio = nombre.strip()
        for museo in self.museos:
            if museo.nombre == nombre_limpio:
                return museo
        return None

    # Requisitos 1 y 12: validar nombre y aforo, en este orden (teclado y archivo)
    def validar_datos_museo(self, nombre: str, aforo):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if self.buscar_museo(nombre) is not None:
            raise ValueError("Ya existe un museo con ese nombre")
        if type(aforo) is not int:
            raise ValueError("El aforo debe ser un número entero")
        if aforo < 1:
            raise ValueError("El aforo debe ser mayor o igual a 1")

    # Requisito 1 y 10: crear un museo sin sobrescribir duplicados
    def crear_museo(self, nombre: str, aforo: int, fecha_inicio: date):
        nombre = nombre.strip()
        self.validar_datos_museo(nombre, aforo)
        museo = Museo(nombre, aforo, fecha_inicio)
        self.museos.append(museo)

    # Requisito 11: museo con el porcentaje de asistencia más alto y más bajo
    # Compara sin redondear y, si hay empate, conserva el que se creó o cargó primero.
    # Devuelve (más_alto, más_bajo), o (None, None) si ningún museo tiene días.
    def comparar_asistencia(self) -> tuple[Museo | None, Museo | None]:
        mas_alto = None
        mas_bajo = None
        for museo in self.museos:
            if len(museo.visitantes) == 0:
                continue
            if mas_alto is None:
                mas_alto = museo
                mas_bajo = museo
                continue
            if museo.calcular_porcentaje_exacto() > mas_alto.calcular_porcentaje_exacto():
                mas_alto = museo
            if museo.calcular_porcentaje_exacto() < mas_bajo.calcular_porcentaje_exacto():
                mas_bajo = museo
        return mas_alto, mas_bajo

    # Requisito 12: cargar museos desde un archivo CSV (nombre;aforo;año;mes;día)
    # Devuelve None si el archivo no existe; si no, (cantidad_cargada, lineas_descartadas)
    # con lineas_descartadas = [(número_de_línea, causa), ...]
    def cargar_museos(self, ruta: str):
        if not os.path.isfile(ruta):
            return None
        cargados = 0
        descartadas = []
        with open(ruta, encoding="utf-8-sig") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                if numero == 1 or linea.strip() == "":
                    continue  # encabezado y líneas vacías
                campos = [campo.strip() for campo in linea.rstrip("\r\n").split(";")]
                if len(campos) != 5:
                    descartadas.append((numero, "La línea no tiene cinco campos"))
                    continue
                nombre, aforo_texto, anio, mes, dia = campos
                if es_entero(aforo_texto):
                    aforo = int(aforo_texto)
                else:
                    aforo = aforo_texto
                try:
                    self.validar_datos_museo(nombre, aforo)
                    fecha = crear_fecha(anio, mes, dia)
                    if fecha is None:
                        raise ValueError("La fecha no es válida")
                    self.crear_museo(nombre, aforo, fecha)
                except ValueError as error:
                    descartadas.append((numero, str(error)))
                    continue
                cargados = cargados + 1
        return cargados, descartadas

    # Requisito 13: cargar visitantes desde un archivo CSV (museo;visitantes)
    # Devuelve None si el archivo no existe; si no, (días_cargados, lineas_descartadas)
    def cargar_visitantes(self, ruta: str):
        if not os.path.isfile(ruta):
            return None
        cargados = 0
        descartadas = []
        with open(ruta, encoding="utf-8-sig") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                if numero == 1 or linea.strip() == "":
                    continue
                campos = [campo.strip() for campo in linea.rstrip("\r\n").split(";")]
                if len(campos) != 2:
                    descartadas.append((numero, "La línea no tiene dos campos"))
                    continue
                museo = self.buscar_museo(campos[0])
                if museo is None:
                    descartadas.append((numero, "No hay un museo con ese nombre"))
                    continue
                if not es_entero(campos[1]):
                    descartadas.append((numero, "Los visitantes deben ser un número entero"))
                    continue
                try:
                    museo.registrar_visitantes(int(campos[1]))
                except ValueError as error:
                    descartadas.append((numero, str(error)))
                    continue
                cargados = cargados + 1
        return cargados, descartadas
