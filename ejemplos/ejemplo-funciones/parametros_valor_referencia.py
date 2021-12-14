#Paso de parámetros por valor (tipo básico)
def funcion1(x):
    x = x + 2

#Paso de parámetros por referencia(objetos)
def funcion2(x):
    x.append(2)

def funcion3(x):
    x = x + " y punto"

numero = 5
lista = [3,8]
texto = "Porque lo digo yo"

funcion1(numero)
funcion2(lista)
funcion3(texto)

print(numero)#5 en lugar de 7
print(lista) #[3,8,2] en lugar de [3,8,2] 
print(texto) #"Porque lo digo yo" en lugar de "Porque lo digo yo y punto"