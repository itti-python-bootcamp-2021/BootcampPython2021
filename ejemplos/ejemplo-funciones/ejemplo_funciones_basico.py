def saluda():
    print("Hola")

def calcular_longitud(nombre):
    print(len(nombre))

def concatenar_palabras(palabra1, palabra2):
    print(palabra1 + palabra2)

def dime_algo():
    return ("Algo")

def suma(sumando1, sumando2):
    resultado = sumando1 + sumando2
    return resultado
    
saluda()
calcular_longitud("Tenerife")
concatenar_palabras("Viva"," el Betis")
concatenar_palabras(3,4)
concatenar_palabras([10,5],[8,15])
concatenar_palabras(["Betis"],[3])
print(dime_algo())
resultado_operacion = suma(8,5)
print(resultado_operacion * 5)

resultado = concatenar_palabras("palabra1","palabra2")#Como la función no tiene retorno, resultado=None
print(resultado)