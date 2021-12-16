import json
import urllib.request
import urllib.parse

KEY = "a9e0dc88"

#{'Response': 'False', 'Error': 'Movie not found!'}

def get_json_from_server(titulo):
    titulo_procesado = urllib.parse.quote_plus(titulo)
    url = f"http://www.omdbapi.com/?apikey={KEY}&t={titulo_procesado}"
    print(url)
    contenido = urllib.request.urlopen(url).read()
    contenido = json.loads(contenido) #Utilizando el método loads
    return contenido

def generar_html(pelicula):
    titulo = pelicula.get("Title")
    anyo = pelicula.get("Year")
    duracion = pelicula.get("Runtime")
    actores = [peli.strip() for peli in pelicula.get("Actors").split(",")]
    poster = pelicula.get("Poster")
    escribir_html(titulo, anyo, duracion, actores, poster)
    
def escribir_html(titulo, anyo, duracion, actores, poster):
    print(titulo)
    with open(titulo.replace(":","-") + ".html","w", encoding="UTF-8") as pagina:
        pagina.write(
f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{titulo}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
""")
        pagina.write(f"<h1 class='titular'>{titulo}</h1>")
        pagina.write("<div class='ficha'>")
        pagina.write(f"<p>Año: {anyo}</p>")
        pagina.write(f"<p>Duración: {duracion}</p>")
        pagina.write("<ul>")
        for actor in actores:
            pagina.write(f"<li>{actor}</li>")
        pagina.write("</ul>")
        pagina.write(f"<img src=\"{poster}\">")
        pagina.write("</div>")
        pagina.write(
"""
</body>
</html>
""")

titulo = input("Introduce un título de película:")
pelicula = get_json_from_server(titulo)
if (pelicula.get("Response")=="False"):
    print("La película no existe")
else:
    generar_html(pelicula)