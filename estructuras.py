class HashMap:
    def __init__(self, capacidad=152):
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
            print("La PC esta vacia")
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