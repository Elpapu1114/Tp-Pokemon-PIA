import random
import time

from pokemon import Pokemon
from algoritmos import busqueda_lineal_equipo
from PC import menu_ordenar_pc
from utils import limpiar


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


def ver_pokedex(pokedex):
    limpiar()
    print()
    print("POKEDEX NACIONAL")
    print()
    pokedex.mostrar()
    print()
    input("Presiona Enter para volver al menu")
    limpiar()


def ver_equipo(equipo):
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
    input("Presiona Enter para volver al menu ")
    limpiar()


def ver_pc(pc):
    limpiar()
    print()
    print("PC")
    print()
    pc.mostrar()
    print()
    input("Presiona Enter para volver al menu ")
    limpiar()


def ver_medallas(medallas):
    limpiar()
    print()
    print(f"Medallas ({len(medallas)} obtenidas)")
    print()
    medallas.mostrar()
    print()
    input("Presiona Enter para volver al menu ")
    limpiar()


def capturar_pokemon(pokedex, equipo, pc):
    limpiar()
    print()
    print("Un Pokemon aparecio")
    print()

    todos = pokedex.values()
    salvaje = random.choice(todos)

    print(f"Es un {salvaje.nombre} ({salvaje.tipo}) | PC: {salvaje.poder_combate}")
    print()

    while True:
        intentar = input("Queres intentar atraparlo? (s/n): ").strip().lower()
        if intentar in ("s", "n"):
            break
        print("Opcion incorrecta, ingresa s o n")

    if intentar == "n":
        print("\nDejaste escapar al Pokemon")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    ids_equipo = {p.id for p in equipo}
    ids_pc = {p.id for p in pc.a_lista()}
    if salvaje.id in ids_equipo or salvaje.id in ids_pc:
        print(f"\nYa tenes un {salvaje.nombre} en tu equipo o PC")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

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

    input("\nPresiona Enter para continuar ")
    limpiar()


def ordenar_pc(pc):
    limpiar()
    menu_ordenar_pc(pc)


def buscar_en_equipo(equipo):
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
                print(f"\n{nombre} no esta en tu equipo")
    input("\nPresiona Enter para continuar ")
    limpiar()


def centro_pokemon(equipo):
    from estructuras import Queue
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
            print(f"Curando a {pokemon.nombre}", end=" ", flush=True)
            time.sleep(0.8)
            print("Listo")

        print()
        print("Todos tus Pokemon fueron curados")

    input("\nPresiona Enter para continuar ")
    limpiar()


def transferir_al_oak(equipo, pc, stack_transferencias):
    limpiar()
    print()
    print("TRANSFERIR AL PROFESOR OAK")
    print()

    tiene_pc = not pc.esta_vacia()

    if not tiene_pc:
        print("No tenes Pokemon para transferir")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    pokemon_a_transferir = None

    if not tiene_pc:
        print("No hay Pokemon en la PC para transferir")
        input("\nPresiona Enter para continuar")
        limpiar()
        return

    print()
    pc.mostrar()
    print()
    lista_pc = pc.a_lista()
    try:
        idx = int(input("Numero del Pokemon a transferir (0 para cancelar): ").strip())
        if idx == 0:
            limpiar()
            return
        idx -= 1
        if not 0 <= idx < len(lista_pc):
            raise ValueError
        seleccionado = lista_pc[idx]
        pokemon_a_transferir = pc.eliminar_por_id(seleccionado.id)
    except ValueError:
        print("\nOpcion invalida")

    if pokemon_a_transferir:
        stack_transferencias.apilar(pokemon_a_transferir)
        print(f"\n{pokemon_a_transferir.nombre} fue transferido al Profesor Oak")
        print(f"(Se guardan las ultimas {len(stack_transferencias)} transferencias para deshacer)")

    input("\nPresiona Enter para continuar ")
    limpiar()


def deshacer_transferencia(equipo, pc, stack_transferencias):
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
        print(f"(Quedan {len(stack_transferencias)} transferencia para deshacer)")

    input("\nPresiona Enter para continuar ")
    limpiar()


def desafiar_gimnasio(equipo, medallas, pokedex):
    limpiar()

    if len(equipo) < 3:
        print()
        print(f"Necesitas al menos 3 Pokemon en tu equipo para desafiar un gimnasio")
        print(f"Tenes {len(equipo)}/3. Captura mas Pokemon primero")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    print()
    print("GIMNASIOS DISPONIBLES")
    print()
    for i, g in enumerate(GIMNASIOS, 1):
        estado = " [MEDALLA OBTENIDA]" if medallas.contiene(g["medalla"]) else ""
        print(f"  {i}. Gimnasio {g["nombre"]} - Lider: {g["lider"]}{estado}")
    print()

    gym_disponible = None
    for g in GIMNASIOS:
        if not medallas.contiene(g["medalla"]):
            gym_disponible = g
            break

    if gym_disponible is None:
        print("Ya obtuviste todas las medallas. Sos el campeon")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    try:
        eleccion = int(input("Ingresa el numero del gimnasio a desafiar: ").strip())
        gym_elegido = GIMNASIOS[eleccion - 1]
    except (ValueError, IndexError):
        print("\nOpcion invalida")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    if gym_elegido != gym_disponible:
        if medallas.contiene(gym_elegido["medalla"]):
            print(f"\nYa obtuviste la {gym_elegido["medalla"]}, no podes desafiarlo de nuevo")
        else:
            print(f"\nDebes derrotar primero al Lider {gym_disponible["lider"]} del Gimnasio {gym_disponible["nombre"]}")
        input("\nPresiona Enter para continuar ")
        limpiar()
        return

    while True:
        confirmar = input(f"\nDesafiar a {gym_disponible["lider"]}? (s/n): ").strip().lower()
        if confirmar in ("s", "n"):
            break
        print("Opcion incorrecta, ingresa s o n")

    if confirmar == "n":
        limpiar()
        return

    gym = gym_disponible
    medalla_en_juego = gym["medalla"]

    tipos_gym = gym["tipos"]
    candidatos = [p for p in pokedex.values() if any(t in p.tipo for t in tipos_gym)]
    if len(candidatos) < 3:
        candidatos = pokedex.values()
    equipo_rival = random.sample(list(candidatos), min(3, len(candidatos)))

    print()
    print(f"Te enfrentas al Lider {gym["lider"]} del Gimnasio {gym["nombre"]}")
    print()
    print("Su equipo: ")
    for p in equipo_rival:
        print(f"    - {p.nombre} ({p.tipo})")

    print()
    print("La batalla ha comenzado.", end="", flush=True)
    time.sleep(2)
    print(" YA")
    time.sleep(1)

    if random.randint(1, 2) == 1:
        print()
        print("Ganaste la batalla")
        if medallas.agregar(medalla_en_juego):
            print(f"Obtuviste la {medalla_en_juego}")
        else:
            print(f"Ya tenias la {medalla_en_juego}. No se duplico")
    else:
        print()
        print("Perdiste la batalla. Entrena mas y volve a intentarlo")

    input("\nPresiona Enter para continuar ")
    limpiar()