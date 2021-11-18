def duplicar(numero):
    return numero*2


#Cola
numeros = [1,3,8,10,3,4,5]
while len(numeros)>0:
    print(duplicar(numeros.pop(0)))

#Pila
numeros = [1,3,8,10,3,4,5]
while len(numeros)>0:
    print(duplicar(numeros.pop(-1)))

#Borrado
numeros = [1,3,8,10,3,4,5]
numeros.remove(10) #Borrando el elemento con valor 10
print(numeros)

#Borrado de todos los 3
numeros = [1,3,8,10,3,4,5]
while 3 in numeros:
    numeros.remove(3)
print(numeros)

#Borrado de todos los 3 (con lambda)
numeros = [1,3,8,10,3,4,5]
print(list(filter(lambda a: a != 3, numeros)))

