numero = 3

def incrementar(numero):
    numero+=2
    return numero

def calcular(numero):
    global resultado
    resultado = numero + 10

def sumar_a_numero():
    global numero
    numero = numero + 5 #Esto es una declaración y si no se usa global, numero sera local
    print(numero)

print(numero)
print(incrementar(8))
calcular(10)
print(resultado)
sumar_a_numero()