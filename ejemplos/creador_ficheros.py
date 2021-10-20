#Abrir fichero
mifichero = open("fichero_salida.txt","w")
#Escribir
for i in range(100):
    mifichero.write("Línea " + str(i))
    mifichero.write("\n")
#Cerrar fichero
mifichero.close()