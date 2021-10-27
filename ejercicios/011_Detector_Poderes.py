import random
numero_secreto = random.randint(1,10)
#Nivel 1
#Pedir al usuario un número hasta que acierte con el número secreto
#Utilizamos bucle while
#Nivel 2
#Si el número de intentos es <=3 le decimos que es un adivino
#Si no, le decimos que es un farsante como adivino
numero_candidato=0
numero_intentos=0
while numero_candidato!=numero_secreto:
    numero_candidato=int(input("Introduce el número candidato entre 1 y 10:"))
    numero_intentos+=1
if (numero_intentos<=3):
    print("Eres un gran adivino")
else:
    print("Lo ha adiviando, pero eres un poco farsante")