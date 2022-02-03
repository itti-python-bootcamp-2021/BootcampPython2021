def saludar():
    return("Hola")

def despedir():
    print("Adios")

i1 = "saludar()"
i2 = "despedir()"
lista_instrucciones = [i1,i2]

for i in lista_instrucciones:
    print(exec(i))