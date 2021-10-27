numero_secreto = 8
numero_candidato = 0
numero_intentos = 0
while (numero_intentos<3):
    numero_intentos+=1
    numero_candidato = int(input("Introduce número candidato:"))
    if (numero_candidato==numero_secreto):
        print("Bravo, eres un gran adivino")
        break
else:
    print("Eres un fraude")