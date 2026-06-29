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