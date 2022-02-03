"""
Diccionario palabras castellano --> traducción al ingléS
lista = ("Casa","Pan","Dinero","Amor")
En caso de que no dispongamos de la solución--> Alternativas: 1. Lanzar una exception; 2. Devolver un texto "Traducción no disponible".
"""
diccionario = {"Casa":"House","Pan":"Bread","Dinero":"Money","Amor":"Love"}

def traducir(palabra):
    if palabra not in diccionario.keys():
        return ("Traducción no disponible")
        #raise Exception("La palabra no existe")
    return diccionario[palabra]

lista_palabras = ("Pan","Dinero","Abejaruco","Amor")

try:
    mapa = map(traducir, lista_palabras)
    lista_palabras_traducidas = list(mapa)
    print(lista_palabras_traducidas)
except Exception as e:
    print(e)
