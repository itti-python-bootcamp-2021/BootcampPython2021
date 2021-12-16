import json

NOMBRE_FICHERO = "indiana_jones.json"
NOMBRE_FICHERO_SALIDA = "enbuscadelarcaperdida.xml"
NOMBRE_FICHERO_SQL = "script.sql"

def get_json_from_file(nombre_fichero):
    with open(nombre_fichero,"r",encoding="UTF-8") as fichero:
        contenido_json = json.load(fichero)
        return contenido_json

def escribir_xml_from_pelicula(nombre_fichero, titulo, anyo, rated):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        fichero.write("<pelicula>")
        fichero.write("<title>" + str(titulo) + "</title>")
        fichero.write("<anyo>" + str(anyo) + "</anyo>")
        fichero.write("<rated>" + rated + "</rated>")
        fichero.write("</pelicula>")

def escribir_insert_sql_from_pelicula(nombre_fichero, titulo, anyo, rated):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write(f"INSERT into TABLAS_PELICULAS (titulo, anyo, rated) VALUES ('{titulo}', '{anyo}', '{rated}')")


json_file = get_json_from_file(NOMBRE_FICHERO)
#Title, Year, Rated
title = json_file.get("Title")
year = json_file.get("Year")
rated = json_file.get("Rated")

escribir_xml_from_pelicula(NOMBRE_FICHERO_SALIDA, title, year, rated)
escribir_insert_sql_from_pelicula(NOMBRE_FICHERO_SQL, title, year, rated)























