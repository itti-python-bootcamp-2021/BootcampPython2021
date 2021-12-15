import urllib.request

contenido = urllib.request.urlopen("http://localhost:80/pelicula.json").read()

print(contenido)