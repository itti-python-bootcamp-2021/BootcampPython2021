with open("datos.txt","r",encoding="UTF-8") as fichero:
    #contenido = fichero.read()#Lee el fichero completo
    #texto = fichero.read(10)#Lee los 10 siguientes bytes
    #linea = fichero.readline()[:-1]#Lee una línea, incluyendo el saldo de línea
    #lineas = fichero.readlines()#Devuelve una lista con todas las líneas
    """
    for linea in fichero:
        print(linea[:-1])
    """
    texto = fichero.read(12)#Leemos 12 bytes. Esto modifica la posición del cursor.
    fichero.seek(5)#Posicionamos el cursor en el 5º byte
    print(fichero.read(3))#Leemos los siguientes 3 bytes a partir del cursor
    