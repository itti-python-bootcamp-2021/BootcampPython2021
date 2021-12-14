NOMBRE_FICHERO="compuesto.txt"
lista_peliculas = []

def get_actores(linea):
    #*Actor 4.1,Actor 4.2,Actor 4.
    linea = linea[1:].split(",")
    return linea

with open(NOMBRE_FICHERO,"r",encoding="UTF-8") as f:
    linea = f.readline()[:-1]
    contador=1
    while(linea!=""):
        if (contador%4==1):
            pelicula = {"titulo":"","director":"","anyo":"","actores":""}
            pelicula["titulo"]=linea
        elif (contador%4==2):
            pelicula["director"]=linea
        elif (contador%4==3):
            pelicula["anyo"]=linea
        elif (contador%4==0):
            pelicula["actores"]=get_actores(linea)
            lista_peliculas.append(pelicula)
        linea = f.readline()
        if linea.endswith('\n'):
            linea = linea[:-1]
        contador+=1
print(lista_peliculas)
    
