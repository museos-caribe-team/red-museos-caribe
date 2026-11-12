from business_logic import (
    crear_museo,
    buscar_museo,
    fecha_siguiente,
    registrar_visitantes,
    simular_dias,
    informe_museo,
    convertir_entero
)


def menu():
    while True:
        print("\nRED DE MUSEOS DEL CARIBE")
        print("1. Crear un museo")
        print("2. Registrar visitantes del día siguiente")
        print("3. Simular días")
        print("4. Ver informe de un museo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del museo: ")
            # Se valida cada dato en el orden indicado por el enunciado.
            nombre_limpio = nombre.strip()
            if nombre_limpio == "":
                print("Error: el nombre no puede estar vacío.")
                continue
            if buscar_museo(nombre_limpio) is not None:
                print("Error: ya existe un museo con ese nombre.")
                continue

            aforo = input("Aforo diario: ")
            numero_aforo = convertir_entero(aforo)
            if numero_aforo is None:
                print("Error: el aforo diario debe ser un número entero.")
                continue
            if numero_aforo < 1:
                print("Error: el aforo diario debe ser de al menos un visitante.")
                continue

            anio = input("Año de inicio: ")
            mes = input("Mes de inicio: ")
            dia = input("Día de inicio: ")
            print(crear_museo(nombre, aforo, anio, mes, dia))

        elif opcion == "2":
            nombre = input("Nombre del museo: ")
            museo = buscar_museo(nombre)
            if museo is None:
                print("Error: no hay un museo con ese nombre.")
                continue

            print("Fecha del siguiente día:", fecha_siguiente(museo))
            while True:
                visitantes = input("Visitantes del día: ")
                resultado = registrar_visitantes(nombre, visitantes)
                print(resultado)
                if not resultado.startswith("Error:"):
                    break

        elif opcion == "3":
            nombre = input("Nombre del museo: ")
            museo = buscar_museo(nombre)
            if museo is None:
                print("Error: no hay un museo con ese nombre.")
                continue

            cantidad = input("Cantidad de días a simular: ")
            numero = convertir_entero(cantidad)
            if numero is None:
                print("Error: el número de días debe ser un número entero.")
                continue
            if numero < 1:
                print("Error: se debe simular al menos un día.")
                continue

            minimo = input("Visitantes mínimos: ")
            minimo_numero = convertir_entero(minimo)
            if minimo_numero is None:
                print("Error: los visitantes deben ser un número entero.")
                continue
            if minimo_numero < 0 or minimo_numero > museo["aforo"]:
                print("Error: los visitantes van de 0 a", museo["aforo"])
                continue

            maximo = input("Visitantes máximos: ")
            maximo_numero = convertir_entero(maximo)
            if maximo_numero is None:
                print("Error: los visitantes deben ser un número entero.")
                continue
            if maximo_numero < 0 or maximo_numero > museo["aforo"]:
                print("Error: los visitantes van de 0 a", museo["aforo"])
                continue
            if minimo_numero > maximo_numero:
                print("Error: el mínimo no puede ser mayor que el máximo.")
                continue

            print(simular_dias(nombre, cantidad, minimo, maximo))

        elif opcion == "4":
            nombre = input("Nombre del museo: ")
            print(informe_museo(nombre))

        elif opcion == "7":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
