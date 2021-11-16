#PASO DE PARÁMETROS POR VALOR
def sumar(s1, s2):
    s1 = s1 + s2

#PASO DE PARÁMETROS POR REFERENCIA
def agregar(lista, numero):
    lista.append(numero) 

sumando1 = 2
sumando2 = 3
sumar(sumando1, sumando2)
print(sumando1)

lista_original=[]
numero=8
agregar(lista_original,numero)
print(lista_original)

