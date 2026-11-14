from datetime import date, timedelta
from random import randint

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


class RedMuseos:

    def __init__(self):
        self.museos = []

    def buscar_museo(self, nombre: str):
        for museo in self.museos:
            if museo.nombre == nombre.strip():
                return museo
        return None

    # Requisito 1: crear un museo
    def crear_museo(self, nombre: str, aforo: int, fecha_inicio: date):
        nombre = nombre.strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if self.buscar_museo(nombre) is not None:
            raise ValueError("Ya existe un museo con ese nombre")
        if type(aforo) is not int:
            raise ValueError("El aforo debe ser un número entero")
        if aforo < 1:
            raise ValueError("El aforo debe ser mayor o igual a 1")
        museo = Museo(nombre, aforo, fecha_inicio)
        self.museos.append(museo)



