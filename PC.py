from algoritmos import bubble_sort_nombre, insertion_sort_tipo, quick_sort_pc
from utils import limpiar


def menu_ordenar_pc(pc):
    if pc.esta_vacia():
        print("La PC esta vacia, no hay nada para ordenar")
        input("\nPresiona Enter para continuar ")
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
        input("Presiona Enter para continuar ")
        return

    print()
    print("PC despues del ordenamiento: ")
    pc.mostrar()
    input("\nPresiona Enter para continuar ")
    limpiar()