"""
Utilizando for:
1. Mostrar los números del 1 al 100
2. Mostrar los números del 100 al 1
3. Mostrar los números pares entre 1 y 50
4. Pedir al usuario dos números pares y mostrar los pares intermedios entre ambos
5. Mostrar los números del 100 al 1 con un paso de -5 
"""
#1
for i in range(1,101):
    print(i)
#2
for i in range(100,0,-1):
    print(i)
#3
for i in range(2,52,2):
    print(i)
#Versión Alejandra
for i in range(1,51):
    if (i%2==0):
        print(i)
#4
par1 = int(input("Introduce el primer número par:"))
par2 = int(input("Introduce el segundo número par:"))
for i in range(par1, par2+1, 2):
    print(i)
#5
for i in range(100,0,-5):
    print(i)
