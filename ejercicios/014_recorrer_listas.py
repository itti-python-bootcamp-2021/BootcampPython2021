"""
Recorrer todos los elementos de una lista al derecho mediante índice
Recorrer todos los elementos de una lista al revés mediante índice
"""
marcas = ['BMW', 'FIAT', 'SEAT', 'RENAULT', 'FERRARI']
print("***")
for i in range(0,len(marcas)):
    print(marcas[i])
print("*** AL REVÉS - OPCIÓN A")
for i in range(-1, -len(marcas)-1, -1):
    print(marcas[i])
print("*** AL REVÉS - OPCIÓN B")
for i in range(len(marcas)-1,-1,-1):
    print(marcas[i])
print("*** AL REVÉS - OPCIÓN JUAN LUIS")
for i in range(1,len(marcas)+1):
    print(marcas[-i])
print("*** AL REVÉS - OPCIÓN JUEVES TARDE")
for i in range(int((len(marcas)-1)*0.5)*2,-1,-1):
    print(marcas[i])