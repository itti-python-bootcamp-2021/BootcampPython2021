def escribir_fichero_texto(nombre_fichero, texto):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write(texto)

def leer_fichero_texto(nombre_fichero):
    with open(nombre_fichero, "r", encoding="UTF-8") as fichero:
        contenido = fichero.read()
    return contenido

def copiar_fichero_texto(fichero_origen, fichero_destino):
    contenido = leer_fichero_texto(fichero_origen)
    escribir_fichero_texto(fichero_destino, contenido)

#Copiar un fichero convertido el contenido a maýusculas o a minúsculas
def copiar_fichero_texto_convertido(fichero_origen, fichero_destino, tipo_conversion):
    contenido_origen = leer_fichero_texto(fichero_origen)
    if (tipo_conversion=="MY"):
        contenido_final = contenido_origen.upper()
    elif (tipo_conversion=="MI"):
        contenido_final = contenido_origen.lower()
    else:
        contenido_final = contenido_origen
    escribir_fichero_texto(fichero_destino, contenido_final)

#escribir_fichero_texto("juanluis.txt","Esto es el contenido del fichero de Juan Luis.\nLeña y cáspitas")
#todo_el_contenido = leer_fichero_texto("juanluis.txt")
#print(todo_el_contenido)
#copiar_fichero_texto("juanluis.txt","copia_jl.txt")

tipo_conversion = input("Introduce MAYUSCULA o MINUSCULA (MY, MI):")
copiar_fichero_texto_convertido("ejemplo_funcion_encapsulada.py","ejemplo_enum.py",tipo_conversion)

"""SOLUICION DE JUAN LUIS
def conversor_mayuscula_minuscula(linea, operacion):
    if (operacion=="MY"):
        linea_o = linea.upper()
    elif (operacion=="MI"):
        linea_o = linea.lower()
    else:
        linea_o = linea
    return linea_o    

def copiar_fichero_texto_convertido(fichero_origen, fichero_destino, funcion):
    origen = open(fichero_origen, "r")
    destino = open(fichero_destino, "w")
    linea = origen.readline()
    destino.write(conversor_mayuscula_minuscula(linea, funcion))
    while (linea!=""):
        linea = origen.readline()
        destino.write(conversor_mayuscula_minuscula(linea, funcion))
    destino.close()
    origen.close()

conversion = input("Introduce MAYUSCULA o MINUSCULA (MY, MI):")
copiar_fichero_texto_convertido("juanluis.txt","modificado.txt", conversion)
"""