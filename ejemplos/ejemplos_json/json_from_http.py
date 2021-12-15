import json
import urllib.request

URL = "http://localhost:80/pelicula.json"

def get_json(url):
    contenido = urllib.request.urlopen(url).read()
    contenido = json.loads(contenido) #Utilizando el método loads
    return contenido

contenido = get_json(URL)#contenido es un diccionario
print(contenido.get("titulo"))
print(contenido.get("director"))
print(contenido.get("anyo"))
creditos = contenido.get("creditos")
for actor in creditos:
    print(actor.get("nombre"))