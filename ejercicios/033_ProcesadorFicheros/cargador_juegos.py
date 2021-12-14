"""
identificador
título
número de jugadores
fecha de publicación
developer
publisher
géneros
calificación
plataforma
autor
(1, 'Halo: Combat Evolved', 4, '11/15/2001', 'Bungie', 'Microsoft Game Studios', '|Shooter|', 'T - Teen', '1', NULL),
(3171, 'Testing New Games Titles Report', NULL, NULL, NULL, NULL, NULL, NULL, '4914', NULL);
"""
NOMBRE_FICHERO = "videojuegos_con_trampas.txt"

def limpiar_campo(campo):
    return campo.replace("'","").strip()

def get_generos(str_generos):
    generos=[]
    if (str_generos!="NULL"):
        generos = str_generos[1:-1].split("|")
    return generos

def get_videojuego(videojuego):
    linea = [limpiar_campo(campo) for campo in videojuego]
    id = int(linea[0])
    titulo = linea[1]
    if (linea[2].isdigit()):
        jugadores = int(linea[2])
    else:
        jugadores = 0
    fecha_publicacion = linea[3]
    developer = linea[4]
    publisher = linea[5]
    generos = get_generos(linea[6])
    calificacion = linea[7]
    print(titulo,linea[8])
    plataforma = int(linea[8])
    autor = linea[9]
    juego = (id, titulo, jugadores, fecha_publicacion, developer, publisher, generos, calificacion, plataforma, autor)
    return juego

def cargar_fichero():
    lista_videojuegos=[]
    with open(NOMBRE_FICHERO, "r", encoding="UTF-8") as fichero:
        while True:
            registro = fichero.readline().strip()
            if (len(registro)==0):
                break
            elif (registro.endswith('\n')):
                registro=registro[1:-3]
            else:
                registro=registro[1:-2]
            registro = registro.replace("., ",".,").replace(", ","ñ").split("ñ")
            print(registro)
            videojuego = get_videojuego(registro)
            lista_videojuegos.append(videojuego)
    return lista_videojuegos
    

videojuegos = cargar_fichero()
for vj in videojuegos:
    print(vj)

"""
registro = "(1252, 'F-Zero', 2, '11/21/1990', 'Nintendo Co., Ltd.', 'Nintendo Co., Ltd.', '|Action|', 'E - Everyone', '6', NULL),"
registro = registro[1:-2]
id = registro[:registro.index(",")]
registro = registro[registro.index("'")+1:]
nombre = registro[:registro.index("'")]
registro = registro[registro.index(", ")+2:]
numero_jugadores = registro[:registro.index(",")]
registro = registro[registro.index("'")+1:]
fecha = registro[:registro.index("'")]
registro = registro[registro.index(", '")+3:]
developer = registro[:registro.index("'")]
print(developer)
"""

