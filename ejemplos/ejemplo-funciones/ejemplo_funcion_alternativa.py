def escribir_fichero_texto(nombre_fichero, texto):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write(texto)

def leer_fichero_texto(nombre_fichero):
    with open(nombre_fichero, "r", encoding="UTF-8") as fichero:
        contenido = fichero.read()
    return contenido

def copiar_fichero_texto_convertido(fichero_origen, fichero_destino, tipo_conversion):
    contenido_origen = leer_fichero_texto(fichero_origen)
    if (tipo_conversion=="MY"):
        contenido_convertido = contenido_origen.upper()
    elif (tipo_conversion=="MI"):
        contenido_convertido = contenido_origen.lower()
    escribir_fichero_texto(fichero_destino, contenido_convertido)

tipo_conversion = ""
conversiones = ("MY","MI")
while tipo_conversion not in conversiones:  
    tipo_conversion = input("Introduce MAYUSCULA o MINUSCULA (MY, MI):")
    if tipo_conversion in conversiones:
        copiar_fichero_texto_convertido("ejemplo_funcion_encapsulada.py","salida.out",tipo_conversion)
    else:
        print("OPCION NO ES CORRECTA")