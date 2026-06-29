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


def ejecutar_menu(pokedex, medallas, equipo, pc, stack_transferencias):
    from acciones import (
        ver_pokedex, ver_equipo, ver_pc, ver_medallas,
        capturar_pokemon, ordenar_pc, buscar_en_equipo,
        centro_pokemon, transferir_al_oak, deshacer_transferencia,
        desafiar_gimnasio,
    )
    from utils import limpiar

    opcion = ""

    while opcion != "12":
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            ver_pokedex(pokedex)

        elif opcion == "2":
            ver_equipo(equipo)

        elif opcion == "3":
            ver_pc(pc)

        elif opcion == "4":
            ver_medallas(medallas)

        elif opcion == "5":
            capturar_pokemon(pokedex, equipo, pc)

        elif opcion == "6":
            ordenar_pc(pc)

        elif opcion == "7":
            buscar_en_equipo(equipo)

        elif opcion == "8":
            centro_pokemon(equipo)

        elif opcion == "9":
            transferir_al_oak(equipo, pc, stack_transferencias)

        elif opcion == "10":
            deshacer_transferencia(equipo, pc, stack_transferencias)

        elif opcion == "11":
            desafiar_gimnasio(equipo, medallas, pokedex)

        elif opcion == "12":
            limpiar()
            print()
            print("Gracias por jugar Pokemon Huergo")
            print()

        else:
            print("\nOpcion invalida. Ingresa un numero del 1 al 12")
            input("Presiona Enter para continuar ")
            limpiar()