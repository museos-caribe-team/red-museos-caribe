from datetime import date
from business_logic import RedMuseos

red = RedMuseos()

while True:
    print("===== RED DE MUSEOS DEL CARIBE =====")
    print("1. Crear museo")
    print("2. Registrar los visitantes del día siguiente")
    print("3. Simular días")
    print("4. El informe de un museo")
    print("5. Mayor y menor ocupación (pendiente)")
    print("6. Cargar archivos (pendiente)")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Requisito 1: validar nombre
        nombre = input("Nombre del museo: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue
        if red.buscar_museo(nombre) is not None:
            print("Error: ya existe un museo con ese nombre.")
            continue

        # Requisito 1: validar aforo antes de pedir la fecha
        try:
            aforo = int(input("Aforo diario: "))
        except ValueError:
            print("Error: el aforo debe ser un número entero.")
            continue
        if aforo < 1:
            print("Error: el aforo debe ser mayor o igual a 1.")
            continue

        # Requisito 1: validar fecha
        try:
            anio = int(input("Año de inicio: "))
            mes = int(input("Mes de inicio: "))
            dia = int(input("Día de inicio: "))
            fecha_inicio = date(anio, mes, dia)
        except ValueError:
            print("Error: la fecha no es válida.")
            continue

        try:
            red.crear_museo(nombre, aforo, fecha_inicio)
            print("Museo creado correctamente.")
        except ValueError as error:
            print("Error:", error)

    elif opcion == "2":
        # Requisito 2: buscar museo
        nombre = input("Nombre del museo: ").strip()
        museo = red.buscar_museo(nombre)
        if museo is None:
            print("Error: no existe un museo con ese nombre.")
            continue

        # Requisito 2: repetir hasta registrar una cantidad válida
        print("Fecha del registro:", museo.calcular_fecha_siguiente())
        registrado = False
        while not registrado:
            try:
                cantidad = int(input("Cantidad de visitantes: "))
                fecha = museo.registrar_visitantes(cantidad)
                print("Visitantes registrados para el", fecha)
                registrado = True
            except ValueError as error:
                print("Error:", error)

    elif opcion == "3":
        # Requisito 3: buscar museo
        nombre = input("Nombre del museo: ").strip()
        museo = red.buscar_museo(nombre)
        if museo is None:
            print("Error: no existe un museo con ese nombre.")
            continue

        # Requisito 3: validar cada dato antes de pedir el siguiente
        try:
            dias = int(input("Número de días a simular: "))
        except ValueError:
            print("Error: los días deben ser un número entero.")
            continue
        if dias < 1:
            print("Error: se debe simular al menos un día.")
            continue

        try:
            minimo = int(input("Visitantes mínimos por día: "))
        except ValueError:
            print("Error: el mínimo debe ser un número entero.")
            continue
        if minimo < 0 or minimo > museo.aforo:
            print(f"Error: el mínimo debe estar entre 0 y {museo.aforo}.")
            continue

        try:
            maximo = int(input("Visitantes máximos por día: "))
        except ValueError:
            print("Error: el máximo debe ser un número entero.")
            continue
        if maximo < 0 or maximo > museo.aforo:
            print(f"Error: el máximo debe estar entre 0 y {museo.aforo}.")
            continue
        if minimo > maximo:
            print("Error: el mínimo no puede ser mayor que el máximo.")
            continue

        museo.simular_dias(dias, minimo, maximo)
        print(dias, "días simulados correctamente.")

    elif opcion == "4":
        # Requisito 4: el informe de un museo
        nombre = input("Nombre del museo: ").strip()
        museo = red.buscar_museo(nombre)
        if museo is None:
            print("Error: no existe un museo con ese nombre.")
            continue

        print("\n===== INFORME DEL MUSEO =====")
        print("Nombre:", museo.nombre)
        print("Aforo diario:", museo.aforo)
        if len(museo.visitantes) == 0:
            print("No tiene días registrados.")
        else:
            print("Días registrados:", len(museo.visitantes))
            print("Visitantes totales:", museo.calcular_total())
            print("Promedio diario:", round(museo.calcular_promedio(), 2))
            print("Porcentaje de asistencia:", museo.calcular_porcentaje(), "%")
            # Requisito 5: la desviación estándar
            print("Desviación estándar:", museo.calcular_desviacion())

    elif opcion == "5" or opcion == "6":
        print("Esta opción será implementada por el equipo.")

    elif opcion == "7":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")

