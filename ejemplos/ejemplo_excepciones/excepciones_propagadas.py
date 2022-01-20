def funcion1(numero):
    return funcion2(numero)

def funcion2(numero):
    return funcion3(numero)

def funcion3(numero):
    resultado = 8/numero
    return resultado

#******************************************
try:
    print(funcion1(0))
except Exception as e:
    print(e)