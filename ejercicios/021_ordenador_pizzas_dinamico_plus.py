def ordenador(pizza):
    return pizza[metodo_ordenacion]

pizza1 = ["Cuatro quesos",12,2000]
pizza2 = ["Pepperoni",10,1900]
pizza3 = ["Hawaiana",9,2000]
pizza4 = ["Barbacoa",12,1700]

pizzas=[pizza1, pizza2, pizza3, pizza4]

while True:
    metodo_ordenacion = int(input("Introduce el campo por el que quieres ordenar(0-2):"))
    if metodo_ordenacion==-1:
        break
    pizzas.sort(reverse=True, key=ordenador)
    print(pizzas)