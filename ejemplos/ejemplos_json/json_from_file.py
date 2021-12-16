import json

PATH = "pelicula.json"

def get_json(path):
    with open(path,"r",encoding="UTF-8") as fichero:
        #Opción 1
        #contenido = fichero.read()
        #contenido = json.loads(contenido) #Utilizamos el método loads
        contenido = json.load(fichero)
        return contenido

contenido = get_json(PATH) #contenido es un diccionario
print(contenido.get("titulo"))
print(contenido.get("director"))
print(contenido.get("anyo"))
actores = contenido.get("creditos")
for actor in actores:
    print(actor.get("nombre"))