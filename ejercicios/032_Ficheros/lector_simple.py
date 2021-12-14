NOMBRE_FICHERO = "simple.txt"
with open(NOMBRE_FICHERO, "r", encoding="UTF-8") as fichero:
    peliculas = []
    while True:
        titulo = fichero.readline()[:-1]
        if (titulo==""):
            break
        director = fichero.readline()[:-1]
        anyo = fichero.readline()[:-1]
        pelicula = (titulo, director, int(anyo))
        peliculas.append(pelicula)
    print(peliculas)