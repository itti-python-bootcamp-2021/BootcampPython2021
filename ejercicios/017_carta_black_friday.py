pedido = []
while True:
    #Pedir al usuario un nombre de producto 
    #Si el nombre de producto es EXIT --> Salimos del bucle
    #Añadir el nombre del producto a la lista
    #Al salir del bucle se ordena la lista y se muestran los datos
    producto = input("Introduce el nombre del producto:")
    if (producto=="EXIT"):
        break
    pedido.append(producto)
pedido.sort()
for item in pedido:
    print(item)
    