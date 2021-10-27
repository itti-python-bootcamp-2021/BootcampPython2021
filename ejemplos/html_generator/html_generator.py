nombre_fichero="Alejandra"
pagina = open(nombre_fichero + ".html","w", encoding="utf-8")#"w" significa write

pagina.write("<!DOCTYPE html>")
pagina.write("<html lang=\"es\">")
pagina.write("\n")
pagina.write("<head><meta charset=\"UTF-8\"><title>Mi página personal</title></head>")
pagina.write("\n")
pagina.write("<body>")
pagina.write("\n")
pagina.write("<h1>Alejandra Aceves Apaño</h1>")
pagina.write("\n")
pagina.write("</body>")
pagina.write("\n")
pagina.write("</html>")

pagina.close()