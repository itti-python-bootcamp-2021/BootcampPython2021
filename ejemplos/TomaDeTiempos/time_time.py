import time

def prueba(lista):
    for l in lista:
        print(l)

lista = list(range(1,10000))
inicio = time.time()
for i in range(10):
    prueba(lista)
fin = time.time()
print(f"El tiempo total empleado es de {fin-inicio} segundos")
