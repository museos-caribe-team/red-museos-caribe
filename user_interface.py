from datetime import date, timedelta
from business_logic import RedMuseos

red = RedMuseos()

while True:
    print("\n===== RED DE MUSEOS DEL CARIBE =====")
    print("1. Crear museo")
    print("2. Registrar los visitantes del día siguiente")
    print("3. Simular días")
    print("4. El informe de un museo")
    print("5. Museo con el porcentaje de asistencia más alto y el más bajo")
    print("6. Cargar los museos y los visitantes desde archivos")
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
        # Requisito 2 y 10: buscar museo
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
        # Requisito 3 y 10: buscar museo
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
        # Requisitos 4 al 9: informe ampliado de un museo
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
            # Requisitos 4 y 5
            print("Días registrados:", len(museo.visitantes))
            print("Visitantes totales:", museo.calcular_total())
            print("Promedio diario:", round(museo.calcular_promedio(), 2))
            print("Porcentaje de asistencia:", museo.calcular_porcentaje(), "%")
            print("Desviación estándar:", museo.calcular_desviacion())

            # Requisito 6
            print("Día de más visitantes:", museo.encontrar_dia_mas_visitantes())
            print("Día de menos visitantes:", museo.encontrar_dia_menos_visitantes())

            # Requisito 7
            baja, media, alta, plena = museo.contar_dias_por_nivel()
            print("Días en asistencia baja:", baja)
            print("Días en asistencia media:", media)
            print("Días en asistencia alta:", alta)
            print("Días en asistencia plena:", plena)

            # Requisito 8
            duracion_racha, inicio_racha = museo.encontrar_racha_baja_mas_larga()
            if duracion_racha == 0:
                print("Racha más larga en asistencia baja: no tuvo ningún día en asistencia baja.")
            else:
                print(f"Racha más larga en asistencia baja: {duracion_racha} días (empezó el {inicio_racha})")

            # Requisito 9
            hoy = date.today()
            ultimo_dia = museo.obtener_ultimo_dia_registrado()
            faltantes = museo.calcular_dias_sin_registrar(hoy)
            print("Último día registrado:", ultimo_dia)
            if faltantes == 0:
                print("Estado del registro: el registro está al día.")
            else:
                desde = ultimo_dia + timedelta(days=1)
                hasta = hoy - timedelta(days=1)
                print(f"Días sin registrar: {faltantes} (del {desde} al {hasta})")

    elif opcion == "5":
        # Requisito 11: museo con el porcentaje de asistencia más alto y más bajo
        mas_alto, mas_bajo = red.comparar_asistencia()
        if mas_alto is None:
            print("Ningún museo tiene días registrados.")
        else:
            print(f"Porcentaje de asistencia más alto: {mas_alto.nombre}, {mas_alto.calcular_porcentaje()} %")
            print(f"Porcentaje de asistencia más bajo: {mas_bajo.nombre}, {mas_bajo.calcular_porcentaje()} %")

    elif opcion == "6":
        # Requisito 12: la carga solo se hace con el programa sin museos
        if len(red.museos) > 0:
            print("Error: la carga solo se hace con el programa sin museos.")
            continue

        ruta_museos = input("Ruta del archivo de museos: ").strip().strip('"')
        resultado = red.cargar_museos(ruta_museos)
        if resultado is None:
            print("Error: el archivo no existe.")
            continue
        cargados, descartadas = resultado
        for numero, causa in descartadas:
            print(f"Línea {numero} descartada: {causa}.")
        print("Museos cargados:", cargados)

        # Requisito 13: archivo de visitantes
        ruta_visitantes = input("Ruta del archivo de visitantes: ").strip().strip('"')
        resultado = red.cargar_visitantes(ruta_visitantes)
        if resultado is None:
            print("Error: el archivo no existe.")
            continue
        cargados, descartadas = resultado
        for numero, causa in descartadas:
            print(f"Línea {numero} descartada: {causa}.")
        print("Días cargados:", cargados)

    elif opcion == "7":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")
