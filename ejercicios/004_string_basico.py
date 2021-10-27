#Pedir al usuario que introduzca un nombre de fichero
nombre_fichero = input("Introduce un nombre de fichero con su extensión:")
#Mostrar la extensión del fichero. Método index()
if "." in nombre_fichero:
    extension = nombre_fichero[nombre_fichero.index("."):]
    print(extension)
else:
    print("No hay extensión") 