import json
from pokemon import Pokemon


def cargar_pokedex(pokedex, ruta="pokedex.json"):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for p in datos:
            pokemon = Pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
            pokedex.agregar(pokemon.id, pokemon)


def cargar_medallas(medallas, ruta="medallas.json"):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        todas = datos["todas"]
        for m in datos["obtenidas"]:
            medallas.agregar(m)
        return todas