titulo = "Indiana Jones"
rated = "Lo que sea"
anyo = 1978
with open("salida.xml","w",encoding="UTF-8") as fichero:
    fichero.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
    fichero.write("<pelicula>")
    fichero.write("<title>" + str(titulo) + "</title>")
    fichero.write("<anyo>" + str(anyo) + "</anyo>")
    fichero.write("<rated>" + rated + "</rated>")
    fichero.write("</pelicula>")