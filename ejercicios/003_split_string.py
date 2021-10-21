#nombre_fichero.pdf
#extraer con slicing la extensión
#extraer con slicing el nombre
#len(?) --> Proporciona la longitud de una colección
nombre_fichero = "nombre_fichero.pdf"
extension = nombre_fichero[len(nombre_fichero)-4:]
print(extension)
nombre = nombre_fichero[:len(nombre_fichero)-4]
print(nombre)
