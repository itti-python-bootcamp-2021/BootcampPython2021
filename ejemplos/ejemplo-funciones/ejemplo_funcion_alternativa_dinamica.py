nombre = "Ramon"

def escribir_fichero_texto(nombre_fichero, texto):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write(texto)

def leer_fichero_texto(nombre_fichero):
    with open(nombre_fichero, "r", encoding="UTF-8") as fichero:
        contenido = fichero.read()
    return contenido

def copiar_fichero_texto_convertido(fichero_origen, fichero_destino, tipo_conversion):
    contenido_origen = leer_fichero_texto(fichero_origen)
    #Se genera una función a partir del tipo de objeto y de una cadena de caracteres 
    conversion = getattr(str, tipo_conversion)
    #Se invoca a la función creada en la línea anterior.
    #En este ejemplo conversion(contenido_origen) es equivalente a contenido_origen.upper() o contenido_origen.lower()
    contenido_convertido = conversion(contenido_origen) 
    escribir_fichero_texto(fichero_destino, contenido_convertido)

tipo_conversion = ""
conversiones = {"MY":"upper","MI":"lower"}
while tipo_conversion not in conversiones.keys():  
    tipo_conversion = input("Introduce MAYUSCULA o MINUSCULA (MY, MI):")
    if tipo_conversion in conversiones.keys():
        copiar_fichero_texto_convertido("ejemplo_funcion_alternativa_dinamica.py",
        "dinamica.txt",conversiones.get(tipo_conversion))
    else:
        print("OPCION NO ES CORRECTA")

