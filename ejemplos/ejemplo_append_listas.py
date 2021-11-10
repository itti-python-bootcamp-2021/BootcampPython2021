videojuegos=[]
videojuegos.append("Zelda Breath of the Wild")
videojuegos.append("Fornite")
videojuegos.append("Call Of Duty")
videojuegos.append("FIFA 2022")

print("***SIN ORDENAR***")
for titulo in videojuegos:
    print("Titulo",titulo)

videojuegos.sort()

print("***ORDENADO***")
for titulo in videojuegos:
    print("Titulo",titulo)
