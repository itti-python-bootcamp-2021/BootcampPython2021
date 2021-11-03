try:
    fichero = open("escritura-fichero.txt","r")
    linea = fichero.readline()
    print(linea)
except FileNotFoundError:
    print("Fichero no encontrado")
finally:
    fichero.close()