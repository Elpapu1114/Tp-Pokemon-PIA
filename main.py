import json
import random
import time
import os

def limpiar():

    os.system("cls")

class Pokemon:

    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate


class Nodo:

    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    def agregar(self, pokemon):

        nuevo = Nodo(pokemon)

        if self.cabeza is None:
            self.cabeza = nuevo

        else:

            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def mostrar(self):

        actual = self.cabeza

        if actual is None:
            print("La PC esta vacia")

        while actual is not None:

            print(actual.pokemon.nombre)

            actual = actual.siguiente


pokedex = {}
medallas = set()
equipo = []
pc = ListaEnlazada()
centro_pokemon = []
transferidos = []

archivo = open("pokedex.json", "r")
datos = json.load(archivo)

for p in datos:

    pokemon = Pokemon(
        p["id"],
        p["nombre"],
        p["tipo"],
        p["poder_combate"]
    )

    pokedex[pokemon.id] = pokemon

archivo.close()

archivo = open("medallas.json", "r")
datos = json.load(archivo)

for medalla in datos:
    medallas.add(medalla)

archivo.close()

opcion = ""

while opcion != "10":

    print()
    print("POKEMON HUERGO")
    print("1 Ver Pokedex")
    print("2 Ver Medallas")
    print("3 Capturar Pokemon")
    print("4 Ver Equipo")
    print("5 Ver PC")
    print("6 Centro Pokemon")
    print("7 Transferir Pokemon")
    print("8 Deshacer Transferencia")
    print("9 Desafiar Gimnasio")
    print("10 Salir")

    opcion = input("Opcion: ")

    if opcion == "1":

        limpiar()


        salir = "n"

        while salir.lower() != "s":
            limpiar()
            print()
            print("POKEDEX")

            for pokemon in pokedex.values():

                print(
                    pokemon.id,
                    pokemon.nombre,
                    pokemon.tipo,
                    pokemon.poder_combate
                )

            salir = input("¿Desea volver al menu? (s/n): ")
        limpiar()

    elif opcion == "2":

        limpiar()

        salir = "n"

        while salir.lower() != "s":
            limpiar()
            print()
            print("MEDALLAS")
            print(medallas)

            salir = input("¿Desea volver al menu? (s/n): ")
        limpiar()
    elif opcion == "3":

        limpiar()

        nombre = input("Nombre del Pokemon: ")

        nuevo = Pokemon(
            999,
            nombre,
            "Normal",
            50
        )

        if len(equipo) < 6:

            equipo.append(nuevo)

            print(nombre, "agregado al equipo")

        else:

            pc.agregar(nuevo)

            print("Equipo lleno")
            print(nombre, "fue enviado a la PC")
        
        limpiar()

    elif opcion == "4":

        limpiar()

        print()

        if len(equipo) == 0:

            print("No tienes Pokemon")

        else:

            for pokemon in equipo:

                print(
                    pokemon.nombre,
                    pokemon.tipo,
                    pokemon.poder_combate
                )

        limpiar()

    elif opcion == "5":
        limpiar()
        print()
        print("PC")
        pc.mostrar()
        limpiar()

    elif opcion == "6":

        limpiar()
        print()

        for pokemon in equipo:
            centro_pokemon.append(pokemon)

        while len(centro_pokemon) > 0:

            pokemon = centro_pokemon.pop(0)

            print(pokemon.nombre, "ha sido curado")
        limpiar()
    elif opcion == "7":

        limpiar()

        if len(equipo) > 0:

            pokemon = equipo.pop()

            transferidos.append(pokemon)

            if len(transferidos) > 5:
                transferidos.pop(0)

            print(pokemon.nombre, "fue transferido al Profesor Oak")

        else:

            print("No hay Pokemon para transferir")
        
        limpiar()

    elif opcion == "8":
        limpiar()
        if len(transferidos) > 0:

            pokemon = transferidos.pop()

            if len(equipo) < 6:

                equipo.append(pokemon)

                print(pokemon.nombre, "ha regresado al equipo")

            else:

                pc.agregar(pokemon)

                print(pokemon.nombre, "ha regresado a la PC")

        else:

            print("No hay transferencias para deshacer")
        
        limpiar()

    elif opcion == "9":

        limpiar()

        entrenador = random.choice([
            "Ash",
            "Gary",
            "Misty",
            "Brock",
            "Cynthia",
            "Leon",
            "Red",
            "Blue"
        ])

        lista_pokemon = list(pokedex.values())

        equipo_rival = random.sample(lista_pokemon, 3)

        print("Te enfrentas a", entrenador)
        print()
        print("Su equipo es:")

        for pokemon in equipo_rival:
            print(pokemon.nombre)

        print()
        print("La batalla ha comenzado...")

        time.sleep(3)

        resultado = random.randint(1, 2)

        if resultado == 1:

            gimnasios = [
                "Roca",
                "Agua",
                "Electrico",
                "Planta",
                "Fantasma",
                "Psiquico",
                "Hielo",
                "Dragon"
            ]

            medalla = "Medalla " + random.choice(gimnasios)

            if medalla in medallas:

                print()
                print("Ganaste la batalla")
                print("Pero ya tenias", medalla)

            else:

                medallas.add(medalla)

                print()
                print("Ganaste la batalla")
                print("Obtuviste", medalla)

        else:

            print()
            print("Perdiste la batalla")

        input("Presiona Enter para continuar...")
        limpiar()

    elif opcion == "10":

        limpiar()

        print("Gracias por jugar Pokemon Huergo")