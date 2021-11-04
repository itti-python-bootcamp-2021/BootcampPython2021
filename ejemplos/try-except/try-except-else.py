entrada = input("Introduce un número:")
try:
    numero = int(entrada)
    resultado = numero * 2    
except:
    print("Ha ocurrido un error")
else:
    print("Resultado:",resultado)
    print("En el final del try")
