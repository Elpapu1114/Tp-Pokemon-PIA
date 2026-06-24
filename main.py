import json
import random
import time
import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


# MODULO 1 - CLASE BASE Y CATALOGO

class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __str__(self):
        return f"{self.id} {self.nombre} {self.tipo} {self.poder_combate}"


class HashMap:
    def __init__(self):
        self._tabla = {}

    def agregar(self, clave, valor):
        self._tabla[clave] = valor

    def obtener(self, clave):
        return self._tabla.get(clave, None)

    def eliminar(self, clave):
        if clave in self._tabla:
            del self._tabla[clave]

    def contiene(self, clave):
        return clave in self._tabla

    def values(self):
        return list(self._tabla.values())

    def mostrar(self):
        for pokemon in self._tabla.values():
            print(pokemon)


class HashSet:
    def __init__(self):
        self._conjunto = set()

    def agregar(self, elemento):
        if elemento in self._conjunto:
            return False
        self._conjunto.add(elemento)
        return True

    def contiene(self, elemento):
        return elemento in self._conjunto

    def eliminar(self, elemento):
        self._conjunto.discard(elemento)

    def mostrar(self):
        if not self._conjunto:
            print("No tenes medallas aun.")
        else:
            for medalla in self._conjunto:
                print(medalla)

    def __len__(self):
        return len(self._conjunto)


# MODULO 2 - GESTION DEL ENTRENADOR

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

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.pokemon)
            actual = actual.siguiente
        return resultado

    def desde_lista(self, lista_pokemon):
        self.cabeza = None
        for pokemon in lista_pokemon:
            self.agregar(pokemon)

    def esta_vacia(self):
        return self.cabeza is None

    def mostrar(self):
        if self.cabeza is None:
            print("La PC esta vacia.")
            return
        actual = self.cabeza
        i = 1
        while actual is not None:
            print(f"{i}. {actual.pokemon}")
            actual = actual.siguiente
            i += 1


class Queue:
    def __init__(self):
        self._cola = []

    def encolar(self, elemento):
        self._cola.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self._cola.pop(0)

    def esta_vacia(self):
        return len(self._cola) == 0

    def __len__(self):
        return len(self._cola)





# MODULO 3 - ORGANIZACION DEL ALMACENAMIENTO

def bubble_sort_nombre(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertion_sort_tipo(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo.lower() > clave.tipo.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def quick_sort_pc(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2].poder_combate
    menores = [p for p in lista if p.poder_combate > pivote]
    iguales = [p for p in lista if p.poder_combate == pivote]
    mayores = [p for p in lista if p.poder_combate < pivote]
    return quick_sort_pc(menores) + iguales + quick_sort_pc(mayores)


def menu_ordenar_pc(pc):
    if pc.esta_vacia():
        print("La PC esta vacia, no hay nada para ordenar.")
        input("Presiona Enter para continuar...")
        return

    limpiar()
    print()
    print("ORDENAR PC")
    print("1. Alfabetico por nombre (Bubble Sort)")
    print("2. Por tipo (Insertion Sort)")
    print("3. Por poder de combate mayor a menor (Quick Sort)")
    print("4. Volver")

    sub = input("Opcion: ").strip()

    lista_temp = pc.a_lista()

    if sub == "1":
        lista_temp = bubble_sort_nombre(lista_temp)
        pc.desde_lista(lista_temp)
        print("PC ordenada alfabeticamente.")
    elif sub == "2":
        lista_temp = insertion_sort_tipo(lista_temp)
        pc.desde_lista(lista_temp)
        print("PC ordenada por tipo.")
    elif sub == "3":
        lista_temp = quick_sort_pc(lista_temp)
        pc.desde_lista(lista_temp)
        print("PC ordenada por poder de combate.")
    elif sub == "4":
        return
    else:
        print("Opcion invalida.")

    print()
    print("PC despues del ordenamiento:")
    pc.mostrar()
    input("Presiona Enter para continuar...")
    limpiar()


# INICIALIZACION DE DATOS

pokedex = HashMap()
medallas = HashSet()
equipo = []
pc = ListaEnlazada()

with open("pokedex.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    for p in datos:
        pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
        pokedex.agregar(pokemon.id, pokemon)

with open("medallas.json", "r", encoding="utf-8") as archivo:
    TODAS_LAS_MEDALLAS = json.load(archivo)


# MENU PRINCIPAL

GIMNASIOS = [
    {"nombre": "Roca",     "lider": "Brock",    "tipos": ["Roca", "Tierra"],           "medalla": "Medalla Roca"},
    {"nombre": "Agua",     "lider": "Misty",    "tipos": ["Agua"],                     "medalla": "Medalla Agua"},
    {"nombre": "Electrico","lider": "Lt. Surge","tipos": ["Electrico", "Eléctrico"],   "medalla": "Medalla Electrico"},
    {"nombre": "Planta",   "lider": "Erika",    "tipos": ["Planta"],                   "medalla": "Medalla Planta"},
    {"nombre": "Veneno",   "lider": "Koga",     "tipos": ["Veneno"],                   "medalla": "Medalla Veneno"},
    {"nombre": "Psiquico", "lider": "Sabrina",  "tipos": ["Psiquico", "Psíquico"],     "medalla": "Medalla Psiquico"},
    {"nombre": "Fuego",    "lider": "Blaine",   "tipos": ["Fuego"],                    "medalla": "Medalla Fuego"},
    {"nombre": "Tierra",   "lider": "Giovanni", "tipos": ["Tierra"],                   "medalla": "Medalla Tierra"},
]

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
    print("8 Desafiar Gimnasio")
    print("9 Ordenar PC")
    print("10 Salir")

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        limpiar()
        salir = ""
        while salir.lower() != "s":
            limpiar()
            print()
            print("POKEDEX NACIONAL")
            print()
            pokedex.mostrar()
            print()
            salir = input("Desea volver al menu? (s/n): ")
        limpiar()

    elif opcion == "2":
        limpiar()
        salir = ""
        while salir.lower() != "s":
            limpiar()
            print()
            print(f"MEDALLAS ({len(medallas)} obtenidas)")
            print()
            medallas.mostrar()
            print()
            salir = input("Desea volver al menu? (s/n): ")
        limpiar()

    elif opcion == "3":
        limpiar()
        print()
        print("POKEDEX NACIONAL")
        print()
        pokedex.mostrar()
        print()
        try:
            id_captura = int(input("Ingresa el ID del Pokemon a capturar: ").strip())
        except ValueError:
            print("ID invalido.")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        encontrado = pokedex.obtener(id_captura)
        if encontrado is None:
            print("No existe un Pokemon con ese ID.")
        else:
            ids_equipo = {p.id for p in equipo}
            ids_pc = {p.id for p in pc.a_lista()}
            if encontrado.id in ids_equipo or encontrado.id in ids_pc:
                print(f"{encontrado.nombre} ya esta en tu equipo o PC.")
            else:
                nuevo = Pokemon(encontrado.id, encontrado.nombre, encontrado.tipo, encontrado.poder_combate)
                if len(equipo) < 6:
                    equipo.append(nuevo)
                    print(f"{nuevo.nombre} fue añadido al equipo.")
                else:
                    pc.agregar(nuevo)
                    print(f"Equipo lleno. {nuevo.nombre} fue enviado a la PC.")

        input("Presiona Enter para continuar...")
        limpiar()

    elif opcion == "4":
        limpiar()
        print()
        print(f"EQUIPO ACTIVO ({len(equipo)}/6)")
        print()
        if not equipo:
            print("No tenes Pokemon en el equipo.")
        else:
            for i, p in enumerate(equipo, 1):
                print(f"{i}. {p}")
        print()
        input("Presiona Enter para continuar...")
        limpiar()

    elif opcion == "5":
        limpiar()
        print()
        print("PC")
        print()
        pc.mostrar()
        print()
        input("Presiona Enter para continuar...")
        limpiar()

    elif opcion == "6":
        limpiar()
        print()
        print("CENTRO POKEMON")
        print()

        if not equipo:
            print("No tenes Pokemon para curar.")
        else:
            cola_curacion = Queue()
            for p in equipo:
                cola_curacion.encolar(p)

            print(f"Curando {len(cola_curacion)} Pokemon...")
            print()
            while not cola_curacion.esta_vacia():
                pokemon = cola_curacion.desencolar()
                print(f"Curando a {pokemon.nombre}...", end=" ", flush=True)
                time.sleep(0.8)
                print("Listo!")

            print()
            print("Todos tus Pokemon fueron curados!")

        input("\nPresiona Enter para continuar...")
        limpiar()

    elif opcion == "7":
        limpiar()
        if not equipo:
            print("No hay Pokemon en el equipo para transferir.")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        print()
        print("EQUIPO ACTUAL")
        for i, p in enumerate(equipo, 1):
            print(f"{i}. {p}")
        print()

        try:
            idx = int(input("Elegí el numero del Pokemon a transferir: ").strip()) - 1
            if not 0 <= idx < len(equipo):
                raise ValueError
        except ValueError:
            print("Opcion invalida.")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        ids_equipo = {p.id for p in equipo}
        ids_pc = {p.id for p in pc.a_lista()}
        ids_propios = ids_equipo | ids_pc
        candidatos = [p for p in pokedex.values() if p.id not in ids_propios]

        if not candidatos:
            print("No hay Pokemon disponibles para intercambiar.")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        recibido = random.choice(candidatos)
        transferido = equipo.pop(idx)
        equipo.insert(idx, recibido)

        print(f"Transferiste a {transferido.nombre} y recibiste a {recibido.nombre}!")
        input("Presiona Enter para continuar...")
        limpiar()

    elif opcion == "8":
        limpiar()

        if len(equipo) < 3:
            print(f"Necesitas al menos 3 Pokemon en tu equipo para desafiar un gimnasio.")
            print(f"Tenes {len(equipo)}/3. Captura mas Pokemon antes.")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        print()
        print("GIMNASIOS DISPONIBLES")
        print()
        for i, g in enumerate(GIMNASIOS, 1):
            obtenida = " (medalla obtenida)" if medallas.contiene(g["medalla"]) else ""
            print(f"{i}. Gimnasio {g['nombre']} - Lider: {g['lider']}{obtenida}")
        print()

        gym_disponible = None
        for g in GIMNASIOS:
            if not medallas.contiene(g["medalla"]):
                gym_disponible = g
                break

        if gym_disponible is None:
            print("Ya obtuviste todas las medallas!")
            input("Presiona Enter para continuar...")
            limpiar()
            continue

        print(f"El proximo gimnasio es: {gym_disponible['nombre']} (Lider: {gym_disponible['lider']})")
        confirmar = input("Desafiar? (s/n): ").strip().lower()
        if confirmar != "s":
            limpiar()
            continue

        gym = gym_disponible
        medalla_en_juego = gym["medalla"]

        tipos_gym = gym["tipos"]
        candidatos = [p for p in pokedex.values() if any(t in p.tipo for t in tipos_gym)]
        if len(candidatos) < 3:
            candidatos = pokedex.values()
        equipo_rival = random.sample(candidatos, 3)

        print()
        print(f"Te enfrentas al Lider {gym['lider']} del Gimnasio {gym['nombre']}!")
        print()
        print("Su equipo:")
        for p in equipo_rival:
            print(f"- {p.nombre} ({p.tipo})")

        print()
        print("La batalla ha comenzado...", end="", flush=True)
        time.sleep(2)
        print(" YA!")
        time.sleep(1)

        if random.randint(1, 2) == 1:
            print()
            print("Ganaste la batalla!")
            if medallas.agregar(medalla_en_juego):
                print(f"Obtuviste la {medalla_en_juego}!")
            else:
                print(f"Ya tenias la {medalla_en_juego}. No se duplico.")
        else:
            print()
            print("Perdiste la batalla.")

        input("\nPresiona Enter para continuar...")
        limpiar()

    elif opcion == "9":
        limpiar()
        menu_ordenar_pc(pc)

    elif opcion == "10":
        limpiar()
        print("Gracias por jugar Pokemon Huergo!")
        print()

    else:
        print("Opcion invalida. Ingresa un numero del 1 al 10.")