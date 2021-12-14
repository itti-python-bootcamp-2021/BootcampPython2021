lista = [3,8,10,12,15,20,25,31,34,38,42,44,47,49,52,53,54,58,61,62,70]

def existe_numero(numero, lista):
    longitud = len(lista)
    if (len(lista)<5):
        return numero in lista
    mitad = int(longitud/2)
    lista1 = lista[:mitad]
    lista2 = lista[mitad:]
    if (numero<lista2[0]):
        return existe_numero(numero, lista1)
    else:
        return existe_numero(numero, lista2)
respuesta = existe_numero(58,lista)
print(respuesta)