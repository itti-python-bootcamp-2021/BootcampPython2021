numero_productos = int(input("Introduce el número de productos:"))
lista_productos = []
for i in range(numero_productos):
    nombre_producto = input("Introduce el producto " + str(i+1) + ":")
    lista_productos.append(nombre_producto)
print(lista_productos)
producto_buscado=""
while producto_buscado.upper()!="SALIR":
    producto_buscado = input("Introduce le nombre del producto a buscar:")
    if producto_buscado.upper()=="SALIR":
        continue
    if producto_buscado in lista_productos:
        print("PRODUCTO EXISTENTE")
    else:
        print("PRODUCTO NO EXISTENTE")    