#Paso de parámetros por valor (tipo básico)
def funcion1(x):
    x = x + 2

#Paso de parámetros por referencia(objetos)
def funcion2(x):
    x.append(2)

numero = 5
lista = [3,8]

funcion1(numero)
funcion2(lista)

print(numero)#5
print(lista) #[3,8]