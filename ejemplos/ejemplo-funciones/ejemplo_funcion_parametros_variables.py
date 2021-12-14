def sumar(edad, *numeros):
    print("Edad:", edad)
    for numero in numeros:
        print("Número:",numero)

sumar(3, 83, 1, 4, 3, 3)

"""
SALIDA DE LA EJECUCIÓN:
Edad: 3
Número: 83
Número: 1
Número: 4
Número: 3
Número: 3
"""