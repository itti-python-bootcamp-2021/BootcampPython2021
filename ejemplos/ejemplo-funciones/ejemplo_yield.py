import time

def obtener_precio(lista_precios, concepto):
    time.sleep(2)
    return lista_precios.get(concepto)

"""
def obtener_precios(lista_precios, lista_productos):
    precios=[]
    for concepto in lista_productos:
        print("Obteniendo precio de",concepto)
        precio = obtener_precio(lista_precios, concepto)
        precios.append(precio)
    return precios
"""
def obtener_precios(lista_precios, lista_productos):
    for concepto in lista_productos:
        print("Obteniendo precio de",concepto)
        precio = obtener_precio(lista_precios, concepto)
        yield precio

lista_precios = {"Pan":35,"Leche":100,"Aceite":200}
lista_productos = ["Pan","Aceite","Leche","Pan","Aceite","Pan"]

precios = obtener_precios(lista_precios, lista_productos)
print("Ya tengo la información")
for precio in precios:
    print("Procesando precio",precio)