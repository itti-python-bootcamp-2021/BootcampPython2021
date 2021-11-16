videojuegos=[]
videojuegos.append("Zelda Breath of the Wild")
videojuegos.append("Fornite")
videojuegos.append("Call Of Duty")
videojuegos.append("FIFA 2022")

sentencia_sql = "SELECT * FROM VIDEJUEGOS WHERE PLATAFORMA='PS5'"

INSERTAR REGISTROS, BORRAR REGISTROS, MODIFICAR REGISTROS, LECTURAS DE REGISTROS
CRUD
INSERT, DELETE, UPDATE, SELECT


print("***SIN ORDENAR***")
for titulo in videojuegos:
    print("Titulo",titulo)

videojuegos.sort()

print("***ORDENADO***")
for titulo in videojuegos:
    print("Titulo",titulo)
