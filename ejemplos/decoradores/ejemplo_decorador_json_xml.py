def convertir_json(funcion):
    def wrapper(*args):
        salida = ""
        for item in args[0]:
            salida = salida + "{'" + item[0] + "':'" + item[1] + "'},"
        funcion(*args)
        print(salida)
    return wrapper

def convertir_xml(funcion):
    def wrapper(*args):
        salida = "<xml>"
        for item in args[0]:
            salida = salida + f"<{item[0]}>{item[1]}<{item[0]}/>"
        salida = salida + "</xml>"
        funcion(*args)
        print(salida)
    return wrapper

@convertir_json
def mostrar(tupla_datos):
    print("El resultado de la conversión de:",tupla_datos)

diccionario = (("titulo","Memorias de África"),)
mostrar(diccionario)

@convertir_json
def mostrar_conocimientos(c):
    print("La tupla original es",c)

conocimientos = (("lenguaje","Python"),("lenguaje","Java"),("lenguaje","C"))
mostrar_conocimientos(conocimientos)