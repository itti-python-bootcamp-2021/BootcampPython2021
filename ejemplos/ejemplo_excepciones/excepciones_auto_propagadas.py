def funcion1(numero):
    return funcion2(numero)

def funcion2(numero):
    return funcion3(numero)

def funcion3(numero):
    try:
        resultado = 8/numero
    except Exception as e:
        print("HA OCURRIDO UN ERROR EN LA FUNCION 3")
        raise e
    else:
        return resultado

#******************************************
try:
    print(funcion1(0))
except Exception as e:
    print("EN EL PRINCIPAL:", e)