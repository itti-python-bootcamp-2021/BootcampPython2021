NUMERO_LINEAS_POR_JUEGO = 4

POSICION_TITULO = 0
POSICION_GENERO = 1
POSICION_PLATAFORMA = 2
POSICION_PRECIO = 3

def espaciar():
    print("***************")
def ordenador_videojuegos(videojuego):
    return videojuego[3]
def obtener_juegos():
    fichero = open("videojuegos.txt","r",encoding="utf-8")
    contenido = fichero.read()
    lines = contenido.splitlines()
    numero_juegos=int(len(lines)/NUMERO_LINEAS_POR_JUEGO)
    juegos = []
    for i in range(numero_juegos):
        offset = i*4
        juego=[lines[0+offset], lines[1+offset], lines[2+offset], float(lines[3+offset])]
        """
        #Alternativa a la línea anterior
        titulo = lines[0+offset]
        genero = lines[1+offset]
        plataforma = lines[2+offset]
        precio = float(lines[3+offset])
        juego.append(titulo)
        juego.append(genero)
        juego.append(plataforma)
        juego.append(precio)
        """
        juegos.append(juego)        
    fichero.close() #Método -- Acción
    return juegos
def mostrar_elementos(juegos):
    for juego in juegos:
        print(juego)
def ordenar_juegos(juegos):
    juegos.sort(key=ordenador_videojuegos)
def obtener_coincidencias(juegos, texto_a_buscar):
    coincidencias=[]
    for juego in juegos:
        if (texto_a_buscar.upper() in juego[0].upper()):
            coincidencias.append(juego)
    return coincidencias
def buscar_juegos(juegos, nombre_plataforma, posicion):
    coincidencias=[]
    for juego in juegos:
        if (nombre_plataforma.upper()==juego[posicion].upper()):
            coincidencias.append(juego)
    return coincidencias

juegos = obtener_juegos()
espaciar()
mostrar_elementos(juegos)
ordenar_juegos(juegos)
espaciar()
mostrar_elementos(juegos)
espaciar()
texto_a_buscar = input("Introduce título de videojuego:")
coincidencias = obtener_coincidencias(juegos, texto_a_buscar)
mostrar_elementos(coincidencias)
espaciar()
coincidencias = buscar_juegos(juegos, "PlayStation 5", POSICION_PLATAFORMA)
mostrar_elementos(coincidencias)
espaciar()
coincidencias = buscar_juegos(juegos, "PlayStation 4", POSICION_PLATAFORMA)
mostrar_elementos(coincidencias)
espaciar()
coincidencias = buscar_juegos(juegos, "Rol", POSICION_GENERO)
mostrar_elementos(coincidencias)