import json

class Pokemon:

    def __init__(self, id, nombre, tipo, pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc


pokedex = {}
medallas = set()

archivo = open("pokedex.json", "r")
datos = json.load(archivo)

for p in datos:
    pokemon = Pokemon(
        p["id"],
        p["nombre"],
        p["tipo"],
        p["pc"]
    )

    pokedex[pokemon.id] = pokemon

archivo.close()

archivo = open("medallas.json", "r")
datos = json.load(archivo)

for medalla in datos:
    medallas.add(medalla)

archivo.close()

opcion = ""

while opcion != "4":

    print()
    print("POKEMON HUERGO")
    print("1 - Ver Pokedex")
    print("2 - Ver Medallas")
    print("3 - Obtener Medalla")
    print("4 - Salir")

    opcion = input("Opcion: ")

    if opcion == "1":

        salir = "n"

        while salir.lower() != "s":

            print()
            print("POKEDEX")

            for pokemon in pokedex.values():

                print(
                    pokemon.id,
                    pokemon.nombre,
                    pokemon.tipo,
                    pokemon.pc
                )

            salir = input("¿Desea volver al menu? (s/n): ")

    elif opcion == "2":

        salir = "n"

        while salir.lower() != "s":

            print()
            print("MEDALLAS")
            print(medallas)

            salir = input("¿Desea volver al menu? (s/n): ")

    elif opcion == "3":

        print()
        print("¡Has derrotado al lider del gimnasio roca!")
        print("Recibes la Medalla Roca.")

        cantidad_antes = len(medallas)

        medallas.add("Medalla Roca")

        cantidad_despues = len(medallas)

        if cantidad_antes == cantidad_despues:

            print("Ya tenias esta medalla.")
            print("Las medallas no pueden repetirse.")

        else:

            print("Medalla agregada con exito.")

    elif opcion == "4":

        print("Gracias por jugar Pokemon Huergo.")

    else:

        print("Opcion incorrecta.")