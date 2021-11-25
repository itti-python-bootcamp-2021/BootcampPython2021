peliculas = {"Star Wars":"George Lucas","2001":"Stanley Kubrick", "El Resplandor":"Stanley Kubrick", "Hombres de negro":"George Lucas"}
pelicula = input("Introduce un título de película:")
#El sistema tiene que responder: NO EXISTE o MOSTRAR EL NOMBRE DEL DIRECTOR
#OPCION 1 - IF IN
if pelicula in peliculas:
    print(peliculas[pelicula])
else:
    print("NO EXISTE")
"""
#OPCION 2 - BLOQUE TRY-EXCEPT
try:
    print(peliculas[pelicula])
except:
    print("NO EXISTE")
"""

director = input("Introduce un nombre de director:")
#El sistema tiene que responder: NO EXISTE o MOSTAR LOS TITULOS DE SUS PELICULAS
lista_peliculas = []
for k,v in peliculas.items():
    if (v==director):
        lista_peliculas.append(k)
if (len(lista_peliculas)==0):
    print("NO EXISTE")
else:
    for peli in lista_peliculas:
        print(peli)