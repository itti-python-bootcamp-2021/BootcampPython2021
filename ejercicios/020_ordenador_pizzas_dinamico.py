def ordenador_por_nombre(pizza):
    return pizza[0]
def ordenador_por_precio(pizza):
    return pizza[1]
def ordenador_por_calorias(pizza):
    return pizza[2]

pizza1 = ["Cuatro quesos",12,2000]
pizza2 = ["Pepperoni",10,1900]
pizza3 = ["Hawaiana",9,2000]
pizza4 = ["Barbacoa",12,1700]

pizzas=[pizza1, pizza2, pizza3, pizza4]
funciones_ordenacion = [ordenador_por_nombre,ordenador_por_precio,ordenador_por_calorias]

while True:
    metodo_ordenacion = int(input("Introduce el campo por el que quieres ordenar(0-2):"))
    if metodo_ordenacion==-1:
        break
    pizzas.sort(key=funciones_ordenacion[metodo_ordenacion])
    print(pizzas)