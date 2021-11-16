def ordenador_peliculas(pelicula):
    return str(pelicula[2])+pelicula[1]

peliculas = []

pelicula1 = ["El resplandor", "Stanley Kubrick", 1980]
pelicula2 = ["El planeta de los simios", "Franklin Schaffner", 1968]
pelicula3 = ["El padrino", "Francis Ford Coppola", 1972]
pelicula4 = ["Le llamaban Trinidad", "Enzo Barboni", 1972]

peliculas.append(pelicula1)
peliculas.append(pelicula2)
peliculas.append(pelicula3)
peliculas.append(pelicula4)

peliculas.sort(reverse=False, key=ordenador_peliculas)
print(peliculas)