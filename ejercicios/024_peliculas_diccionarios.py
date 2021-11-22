pelicula1 = ("Harry Potter 1 - La piedra filosofal",2001,"Warner Bross",("Harry Potter","El chico pelirrojo","La niña empollona"))
pelicula2 = ("Los Simpsons",2010,"Julio Iglesias",("Bart","Maggie","Homer"))
pelicula3 = ("Película 3",2001,"Juan Luis Guerra",("Actor 1","Actor 2","Actor 3","Actor 4"))

peliculas = {pelicula1[0]:pelicula1,pelicula2[0]:pelicula2,pelicula3[0]:pelicula3}

titulo = input("Introduce un título:")
pelicula_buscada = peliculas.get(titulo)
for actor in pelicula_buscada[3]:
    print(actor)

peliculas.keys()#Obtenemos todas las claves
peliculas.values()#Obtenemos todos los valores
peliculas.items()#Obtenemso todos los pares clave-valor
