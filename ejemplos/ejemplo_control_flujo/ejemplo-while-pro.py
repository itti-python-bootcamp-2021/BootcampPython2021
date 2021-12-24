#break, continue
numero_secreto = 8
numero_candidato = 0
while True:
    numero_candidato = int(input("Introduce número candidato:"))
    if (numero_candidato==numero_secreto):
        break
    else:
        pass
    print("Este código nunca se va a ejecutar")
print("Bravo, eres un gran adivino")