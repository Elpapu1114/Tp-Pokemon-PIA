import json
import random
import time
import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __str__(self):
        return f"[#{self.id}] {self.nombre} | Tipo: {self.tipo} | PC: {self.poder_combate}"


class HashMap:
    def __init__(self, capacidad=27):
        self.capacidad = capacidad
        self.buckets = [[] for _ in range(capacidad)]

    def _hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key, value):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def obtener(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def eliminar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def contiene(self, key):
        return self.obtener(key) is not None

    def values(self):
        resultado = []
        for bucket in self.buckets:
            for k, v in bucket:
                resultado.append(v)
        return resultado

    def mostrar(self):
        for bucket in self.buckets:
            for k, v in bucket:
                print(v)


class HashSet:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.buckets = [[] for _ in range(capacidad)]

    def _hash(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        if key in bucket:
            return False
        bucket.append(key)
        return True

    def contiene(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        return key in bucket

    def eliminar(self, key):
        indice = self._hash(key)
        bucket = self.buckets[indice]
        if key in bucket:
            bucket.remove(key)

    def mostrar(self):
        elementos = []
        for bucket in self.buckets:
            for key in bucket:
                elementos.append(key)
        if not elementos:
            print("No tenes medallas aun")
        else:
            for medalla in sorted(elementos):
                print(f"  - {medalla}")

    def __len__(self):
        total = 0
        for bucket in self.buckets:
            total += len(bucket)
        return total


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

    def eliminar_por_id(self, id_pokemon):
        if self.cabeza is None:
            return None
        if self.cabeza.pokemon.id == id_pokemon:
            eliminado = self.cabeza.pokemon
            self.cabeza = self.cabeza.siguiente
            return eliminado
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.pokemon.id == id_pokemon:
                eliminado = actual.siguiente.pokemon
                actual.siguiente = actual.siguiente.siguiente
                return eliminado
            actual = actual.siguiente
        return None

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
            print(f"  {i}. {actual.pokemon}")
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


class Stack:
    CAPACIDAD_MAXIMA = 5

    def __init__(self):
        self._pila = []

    def apilar(self, pokemon):
        if len(self._pila) >= self.CAPACIDAD_MAXIMA:
            self._pila.pop(0)   
        self._pila.append(pokemon)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self._pila.pop()

    def esta_vacia(self):
        return len(self._pila) == 0

    def __len__(self):
        return len(self._pila)


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
        print("La PC esta vacia, no hay nada para ordenar")
        input("\nPresiona Enter para continuar")
        return

    limpiar()
    print()
    print("ORDENAR PC")
    print("1. Alfabetico por nombre")
    print("2. Por tipo")
    print("3. Por poder de combate mayor a menor")
    print("4. Volver")
    print()

    sub = input("Opcion: ").strip()
    lista_temp = pc.a_lista()

    if sub == "1":
        lista_temp = bubble_sort_nombre(lista_temp)
        pc.desde_lista(lista_temp)
        print("\nPC ordenada alfabeticamente por nombre")
    elif sub == "2":
        lista_temp = insertion_sort_tipo(lista_temp)
        pc.desde_lista(lista_temp)
        print("\nPC ordenada por tipo")
    elif sub == "3":
        lista_temp = quick_sort_pc(lista_temp)
        pc.desde_lista(lista_temp)
        print("\nPC ordenada por poder de combate")
    elif sub == "4":
        return
    else:
        print("\nOpcion invalida")
        input("Presiona Enter para continuar")
        return

    print()
    print("PC despues del ordenamiento:")
    pc.mostrar()
    input("\nPresiona Enter para continuar")
    limpiar()


def busqueda_lineal_equipo(equipo, nombre):
    for i, p in enumerate(equipo):
        if p.nombre.lower() == nombre.lower():
            return i, p
    return -1, None


def busqueda_binaria_pokedex(ids_ordenados, id_buscado):
    izquierda = 0
    derecha = len(ids_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if ids_ordenados[medio] == id_buscado:
            return medio
        elif ids_ordenados[medio] < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


def menu_busquedas(equipo, pokedex):
    limpiar()
    print()
    print("BUSQUEDAS")
    print("1. Buscar Pokemon en el equipo")
    print("2. Consultar Pokemon en la Pokedex por ID")
    print("3. Volver")
    print()

    sub = input("Opcion: ").strip()

    if sub == "1":
        print()
        nombre = input("Nombre del Pokemon a buscar: ").strip()
        if not nombre:
            print("Nombre invalido")
        else:
            pos, encontrado = busqueda_lineal_equipo(equipo, nombre)
            if encontrado:
                print(f"\n{encontrado.nombre} esta en tu equipo en la posicion {pos + 1}.")
                print(f"{encontrado}")
            else:
                print(f"\n{nombre} no esta en tu equipo.")

    elif sub == "2":
        print()
        try:
            id_buscado = int(input("Ingresa el ID a buscar: ").strip())
        except ValueError:
            print("ID invalido")
            input("\nPresiona Enter para continuar")
            limpiar()
            return

        ids_ordenados = sorted(pokedex._tabla.keys())
        pos = busqueda_binaria_pokedex(ids_ordenados, id_buscado)
        if pos != -1:
            pokemon = pokedex.obtener(ids_ordenados[pos])
            print(f"\nPokemon encontrado: {pokemon}")
        else:
            print(f"\nNo existe un Pokemon con ID {id_buscado} en la Pokedex")

    elif sub == "3":
        limpiar()
        return
    else:
        print("Opcion invalida")

    input("\nPresiona Enter para continuar")
    limpiar()


pokedex = HashMap()
medallas = HashSet()
equipo = []        
pc = ListaEnlazada()
stack_transferencias = Stack()   

with open("pokedex.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    for p in datos:
        pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
        pokedex.agregar(pokemon.id, pokemon)

with open("medallas.json", "r", encoding="utf-8") as archivo:
    datos_medallas = json.load(archivo)
    TODAS_LAS_MEDALLAS = datos_medallas["todas"]
    for m in datos_medallas["obtenidas"]:
        medallas.agregar(m)

GIMNASIOS = [
    {"nombre": "Roca",      "lider": "Brock",     "tipos": ["Roca", "Tierra"],         "medalla": "Medalla Roca"},
    {"nombre": "Agua",      "lider": "Misty",     "tipos": ["Agua"],                   "medalla": "Medalla Agua"},
    {"nombre": "Electrico", "lider": "Lt. Surge", "tipos": ["Electrico", "Electrico"], "medalla": "Medalla Electrico"},
    {"nombre": "Planta",    "lider": "Erika",     "tipos": ["Planta"],                 "medalla": "Medalla Planta"},
    {"nombre": "Veneno",    "lider": "Koga",      "tipos": ["Veneno"],                 "medalla": "Medalla Veneno"},
    {"nombre": "Psiquico",  "lider": "Sabrina",   "tipos": ["Psiquico", "Psiquico"],   "medalla": "Medalla Psiquico"},
    {"nombre": "Fuego",     "lider": "Blaine",    "tipos": ["Fuego"],                  "medalla": "Medalla Fuego"},
    {"nombre": "Tierra",    "lider": "Giovanni",  "tipos": ["Tierra"],                 "medalla": "Medalla Tierra"},
]


def mostrar_menu():
    print()
    print("POKEMON HUERGO")
    print("1.  Ver Pokedex")
    print("2.  Ver Equipo Principal")
    print("3.  Ver PC")
    print("4.  Ver Medallas")
    print("5.  Capturar nuevo Pokemon")
    print("6.  Ordenar PC")
    print("7.  Buscar Pokemon en Equipo")
    print("8.  Enviar Pokemon al Centro Pokemon")
    print("9.  Transferir Pokemon al Profesor Oak")
    print("10.  Deshacer ultima transferencia")
    print("11.  Desafiar Lider de Gimnasio")
    print("12.  Salir del sistema")
    print()


opcion = ""

while opcion != "12":
    mostrar_menu()
    opcion = input("Opcion: ").strip()

    if opcion == "1":
        limpiar()
        print()
        print("POKEDEX NACIONAL")
        print()
        pokedex.mostrar()
        print()
        input("Presiona Enter para volver al menu")
        limpiar()

    elif opcion == "2":
        limpiar()
        print()
        print(f"EQUIPO ACTIVO ({len(equipo)}/6)")
        print()
        if not equipo:
            print("No tenes Pokemon en el equipo")
        else:
            for i, p in enumerate(equipo, 1):
                print(f"  {i}. {p}")
        print()
        input("Presiona Enter para volver al menu")
        limpiar()

    elif opcion == "3":
        limpiar()
        print()
        print("PC")
        print()
        pc.mostrar()
        print()
        input("Presiona Enter para volver al menu")
        limpiar()

    elif opcion == "4":
        limpiar()
        print()
        print(f"MEDALLAS ({len(medallas)} obtenidas)")
        print()
        medallas.mostrar()
        print()
        input("Presiona Enter para volver al menu")
        limpiar()

    elif opcion == "5":
        limpiar()
        print()
        print("Un Pokemon aparecio")
        print()

        todos = pokedex.values()
        salvaje = random.choice(todos)

        print(f"Es un {salvaje.nombre} ({salvaje.tipo}) | PC: {salvaje.poder_combate}")
        print()

        intentar = input("Querés intentar atraparlo? (s/n): ").strip().lower()

        if intentar != "s":
            print("\nDejaste escapar al Pokemon")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        ids_equipo = {p.id for p in equipo}
        ids_pc = {p.id for p in pc.a_lista()}
        if salvaje.id in ids_equipo or salvaje.id in ids_pc:
            print(f"\nYa tenes un {salvaje.nombre} en tu equipo o PC")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        print("\nTirando la pokeball", end="", flush=True)
        time.sleep(1)
        if random.random() < 0.65:
            nuevo = Pokemon(salvaje.id, salvaje.nombre, salvaje.tipo, salvaje.poder_combate)
            if len(equipo) < 6:
                equipo.append(nuevo)
                print(f"\nAtrapaste a {nuevo.nombre}. Fue añadido al equipo ({len(equipo)}/6)")
            else:
                pc.agregar(nuevo)
                print(f"\nAtrapaste a {nuevo.nombre}. Equipo lleno, fue enviado a la PC")
        else:
            print(f"\n{salvaje.nombre} escapo. Mas suerte la proxima")

        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "6":
        limpiar()
        menu_ordenar_pc(pc)

    elif opcion == "7":
        limpiar()
        print()
        print("BUSCAR EN EQUIPO")
        print()
        if not equipo:
            print("No tenes Pokemon en el equipo")
        else:
            nombre = input("Nombre del Pokemon a buscar: ").strip()
            if not nombre:
                print("Nombre invalido")
            else:
                pos, encontrado = busqueda_lineal_equipo(equipo, nombre)
                if encontrado:
                    print(f"\n{encontrado.nombre} esta en tu equipo en la posicion {pos + 1}.")
                    print(f"{encontrado}")
                else:
                    print(f"\n  {nombre} no esta en tu equipo")
        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "8":
        limpiar()
        print()
        print("CENTRO POKEMON")
        print()

        if not equipo:
            print("No tenes Pokemon en el equipo para curar")
        else:
            cola_curacion = Queue()
            for p in equipo:
                cola_curacion.encolar(p)

            print(f"Curando {len(cola_curacion)} Pokemon en cola")
            print()
            while not cola_curacion.esta_vacia():
                pokemon = cola_curacion.desencolar()
                print(f"  Curando a {pokemon.nombre}...", end=" ", flush=True)
                time.sleep(0.8)
                print("Listo")

            print()
            print("Todos tus Pokemon fueron curados")

        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "9":
        limpiar()
        print()
        print("TRANSFERIR AL PROFESOR OAK")
        print()

        tiene_equipo = len(equipo) > 0
        tiene_pc = not pc.esta_vacia()

        if not tiene_equipo and not tiene_pc:
            print("No tenes Pokemon para transferir")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        print("Desde donde queres transferir?")
        print("1. Equipo")
        print("2. PC")
        print("3. Cancelar")
        print()
        origen = input("Opcion: ").strip()

        pokemon_a_transferir = None

        if origen == "1":
            if not tiene_equipo:
                print("\nNo tenes Pokemon en el equipo")
            else:
                print()
                for i, p in enumerate(equipo, 1):
                    print(f"  {i}. {p}")
                print()
                try:
                    idx = int(input("Numero del Pokemon a transferir: ").strip()) - 1
                    if not 0 <= idx < len(equipo):
                        raise ValueError
                    pokemon_a_transferir = equipo.pop(idx)
                except ValueError:
                    print("\nOpcion invalida")

        elif origen == "2":
            if not tiene_pc:
                print("\nNo hay Pokemon en la PC")
            else:
                print()
                pc.mostrar()
                print()
                lista_pc = pc.a_lista()
                try:
                    idx = int(input("Numero del Pokemon a transferir: ").strip()) - 1
                    if not 0 <= idx < len(lista_pc):
                        raise ValueError
                    seleccionado = lista_pc[idx]
                    pokemon_a_transferir = pc.eliminar_por_id(seleccionado.id)
                except ValueError:
                    print("\nOpcion invalida")

        elif origen == "3":
            limpiar()
            continue
        else:
            print("\nOpcion invalida")

        if pokemon_a_transferir:
            stack_transferencias.apilar(pokemon_a_transferir)
            print(f"\n{pokemon_a_transferir.nombre} fue transferido al Profesor Oak")
            print(f"(Se guardan las ultimas {len(stack_transferencias)} transferencia(s) para deshacer)")

        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "10":
        limpiar()
        print()
        print("DESHACER ULTIMA TRANSFERENCIA")
        print()

        if stack_transferencias.esta_vacia():
            print("No hay transferencias para deshacer")
        else:
            recuperado = stack_transferencias.desapilar()
            if len(equipo) < 6:
                equipo.append(recuperado)
                print(f"{recuperado.nombre} fue recuperado y volvio a tu equipo")
            else:
                pc.agregar(recuperado)
                print(f"Equipo lleno. {recuperado.nombre} fue recuperado y enviado a la PC")
            print(f"(Quedan {len(stack_transferencias)} transferencia(s) para deshacer)")

        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "11":
        limpiar()

        if len(equipo) < 3:
            print()
            print(f"Necesitas al menos 3 Pokemon en tu equipo para desafiar un gimnasio")
            print(f"Tenes {len(equipo)}/3. Captura mas Pokemon primero")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        print()
        print("GIMNASIOS DISPONIBLES")
        print()
        for i, g in enumerate(GIMNASIOS, 1):
            estado = " [MEDALLA OBTENIDA]" if medallas.contiene(g["medalla"]) else ""
            print(f"  {i}. Gimnasio {g['nombre']} - Lider: {g['lider']}{estado}")
        print()

        gym_disponible = None
        for g in GIMNASIOS:
            if not medallas.contiene(g["medalla"]):
                gym_disponible = g
                break

        if gym_disponible is None:
            print("Ya obtuviste todas las medallas. Sos el campeon")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        try:
            eleccion = int(input("Ingresa el numero del gimnasio a desafiar: ").strip())
            gym_elegido = GIMNASIOS[eleccion - 1]
        except (ValueError, IndexError):
            print("\nOpcion invalida")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        if gym_elegido != gym_disponible:
            if medallas.contiene(gym_elegido["medalla"]):
                print(f"\nYa obtuviste la {gym_elegido['medalla']}, no podes desafiarlo de nuevo")
            else:
                print(f"\nDebes derrotar primero al Lider {gym_disponible['lider']} del Gimnasio {gym_disponible['nombre']}")
            input("\nPresiona Enter para continuar")
            limpiar()
            continue

        confirmar = input(f"\nDesafiar a {gym_disponible['lider']}? (s/n): ").strip().lower()
        if confirmar != "s":
            limpiar()
            continue

        gym = gym_disponible
        medalla_en_juego = gym["medalla"]

        tipos_gym = gym["tipos"]
        candidatos = [p for p in pokedex.values() if any(t in p.tipo for t in tipos_gym)]
        if len(candidatos) < 3:
            candidatos = pokedex.values()
        equipo_rival = random.sample(list(candidatos), min(3, len(candidatos)))

        print()
        print(f"Te enfrentas al Lider {gym['lider']} del Gimnasio {gym['nombre']}")
        print()
        print("Su equipo:")
        for p in equipo_rival:
            print(f"    - {p.nombre} ({p.tipo})")

        print()
        print("La batalla ha comenzado.", end="", flush=True)
        time.sleep(2)
        print(" YA!")
        time.sleep(1)

        if random.randint(1, 2) == 1:
            print()
            print("Ganaste la batalla")
            if medallas.agregar(medalla_en_juego):
                print(f"Obtuviste la {medalla_en_juego}!")
            else:
                print(f"Ya tenias la {medalla_en_juego}. No se duplico")
        else:
            print()
            print("Perdiste la batalla. Entrena mas y volve a intentarlo")

        input("\nPresiona Enter para continuar")
        limpiar()

    elif opcion == "12":
        limpiar()
        print()
        print("Gracias por jugar Pokemon Huergo")
        print()

    else:
        print("\nOpcion invalida. Ingresa un numero del 1 al 12")
        input("Presiona Enter para continuar")
        limpiar()