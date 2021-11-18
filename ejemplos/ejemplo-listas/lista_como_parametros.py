#numero se pasa por valor y lista se pasa por referencia
def hacer_cosas(numero, lista):
    numero = numero * 2
    lista.append(101)

x = 23
l = [1,2,3,4,5]
hacer_cosas(x,l)
print(x) # 46? 23?
print(l) # 1,2,3,4,5,101? 1,2,3,4,5?