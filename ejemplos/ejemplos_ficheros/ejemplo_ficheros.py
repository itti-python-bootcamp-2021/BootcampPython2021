#with open("datos.txt","r",encoding="UTF-8") as fichero:
    #contenido = fichero.read()#Lee el fichero completo
    #texto = fichero.read(10)#Lee los 10 siguientes bytes
    #linea = fichero.readline()[:-1]#Lee una línea, incluyendo el saldo de línea
    #lineas = fichero.readlines()#Devuelve una lista con todas las líneas
"""
for linea in fichero:
    print(linea[:-1])
"""
    #texto = fichero.read(12)#Leemos 12 bytes. Esto modifica la posición del cursor.
    #fichero.seek(5)#Posicionamos el cursor en el 5º byte
    #print(fichero.read(3))#Leemos los siguientes 3 bytes a partir del cursor
"""
try:
    with open("otrosdatos.txt","x",encoding="UTF-8") as fichero:
            fichero.write("Hola")
except FileExistsError as error:
    print("Ha ocurrido un error: el fichero ya existe")
"""
#Copiar el fichero fichero.pdf como fichero_copia.pdf

"""
#Copiador de ficheros binarios
with open("fichero.pdf","rb") as fichero_pdf:
    with open("fichero_copia.pdf","wb") as copia_fichero_pdf:
        byte = fichero_pdf.read(1)
        while byte==True:
            copia_fichero_pdf.write(byte)
            byte = fichero_pdf.read(1)
print("Terminado")
"""
#Manejo de exceptions relacionadas con el fichero
"""
try:
    fichero = open("datosx.txt","r",encoding="UTF-8")
    datos = fichero.read()
    print(datos)
    fichero.close()
except FileNotFoundError as error:
    print("Fichero no encontrado")
except IOError:
    print("Error de entrada/salida")
"""

with open("datos.txt","r",encoding="UTF-8") as fichero:
    for linea in fichero:
        print(linea[:-1])
