from estructuras import HashMap, HashSet, ListaEnlazada, Stack
from datos import cargar_pokedex, cargar_medallas
from menu import ejecutar_menu


def main():
    pokedex = HashMap()
    medallas = HashSet()
    equipo = []
    pc = ListaEnlazada()
    stack_transferencias = Stack()

    cargar_pokedex(pokedex)
    cargar_medallas(medallas)

    ejecutar_menu(pokedex, medallas, equipo, pc, stack_transferencias)


if __name__ == "__main__":
    main()