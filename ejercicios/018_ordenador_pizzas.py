def ordenador_pizzas(pizza):
    return pizza[2]+pizza[1]#2012 (para pizza 1)-OK
    #return str(pizza[2])+str(pizza[1])#"200012" (para pizza 1)-ERROR

pizza1 = ["Cuatro quesos",12,2000]
pizza2 = ["Pepperoni",10,1900]
pizza3 = ["Hawaiana",9,2000]
pizza4 = ["Barbacoa",12,1700]

pizzas=[pizza1, pizza2, pizza3, pizza4]

pizzas.sort(key=ordenador_pizzas)

print(pizzas)
