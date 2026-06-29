class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.poder_combate = poder_combate

    def __str__(self):
        return f"[#{self.id}] {self.nombre} | Tipo: {self.tipo} | PC: {self.poder_combate}"