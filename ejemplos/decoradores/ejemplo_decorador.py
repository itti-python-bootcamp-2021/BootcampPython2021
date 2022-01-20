def asteriscar(funcion):
    def wrapper(*args):
        adorno = ""
        for i in range(10):
            adorno+=args[0]
        print(adorno)
        retorno = funcion(args[0])
        print(adorno)
        return retorno
    return wrapper

@asteriscar
def saludar(simbolo):
    print("Hola " + simbolo)
    return "OK"

@asteriscar
def despedir(simbolo):
    print("Adios " + simbolo)
    return "KO"

retorno = saludar("+")
print(retorno)
retorno = despedir("*")
print(retorno)