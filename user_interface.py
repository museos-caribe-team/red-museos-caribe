from business_logic import crear_museo


def menu():
    while True:
        print("RED DE MUSEOS DEL CARIBE")
        print("1. Crear museo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del museo: ")

            try:
                aforo = int(input("Aforo diario: "))
                anio = int(input("Año de inicio: "))
                mes = int(input("Mes de inicio: "))
                dia = int(input("Día de inicio: "))
            except ValueError:
                print("Error: debe ingresar números enteros.")
                continue

            resultado = crear_museo(
                nombre, aforo, anio, mes, dia
            )
            print(resultado)

        elif opcion == "7":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
