NOMBRE_FICHERO="compuesto.txt"
lista_peliculas = []

with open(NOMBRE_FICHERO,"r",encoding="UTF-8") as f:
    while (True):
        titulo = f.readline()[:-1]
        if (titulo==""):
            break
        director = f.readline()[:-1]
        anyo = f.readline()[:-1]
        actores = f.readline()[1:]
        if actores.endswith('\n'):
            actores = actores[:-1]
        actores = actores.split(",")
        pelicula = (titulo, director, int(anyo), actores)
        lista_peliculas.append(pelicula)

print(lista_peliculas)