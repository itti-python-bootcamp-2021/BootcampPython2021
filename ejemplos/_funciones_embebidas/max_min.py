class Ordenador:
    def __init__(self, fabricante, velocidad, gigas) -> None:
        self.fabricante = fabricante
        self.velocidad = velocidad
        self.gigas = gigas

    def __lt__(self, other):
        return self.gigas < other.gigas

    def __gt__(self, other, criterio):
        return self.gigas > other.gigas

    def __str__(self) -> str:
        return self.fabricante

    def __repr__(self) -> str:
        return self.fabricante + ":" + str(self.gigas)

o1 = Ordenador("IBM", 10000, 64)
o2 = Ordenador("HP", 5000, 16)
o3 = Ordenador("DELL", 8000, 32)
ordenadores = (o1, o2, o3)
print("Max:", max(ordenadores))

ordenadores_ordenados = sorted(ordenadores)
for o in ordenadores_ordenados:
    print(o)