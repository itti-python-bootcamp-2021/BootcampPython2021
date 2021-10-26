import random
numero_secreto = random.randint(1,1000)
#Nivel 1
#Pedir al usuario un número hasta que acierte con el número secreto
#Utilizamos bucle while
#Nivel 2
#Si el número de intentos es <=3 le decimos que es un adivino
#Si no, le decimos que es un farsante como adivino
numero_candidato=0
while numero_candidato!=numero_secreto:
    numero_candidato = int(input("Introduce el número candidato entre 1 y 10:"))