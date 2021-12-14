"""
[3,4,8,10]
Crea una lista con la suma de los 4 números primeros números,
de los 3 primeros números, de los 2 primeros números y
del primero. 
[25,15,7,3]
"""

def calcular_sumas(lista_inicial, lista_final):
    resultado = 0
    for numero in lista_inicial:
        resultado = resultado + numero
    lista_final.append(resultado)
    lista_inicial.pop()
    if (len(lista_inicial)!=0):
        calcular_sumas(lista_inicial, lista_final)

lista_inicial = [3,4,8,10]
lista_final=[]
calcular_sumas(lista_inicial, lista_final)
print(lista_final)