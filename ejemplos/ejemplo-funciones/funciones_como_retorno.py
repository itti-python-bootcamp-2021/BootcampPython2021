import random

def explotar():
    print("Explotando...")

def encender():
    print("Encendiendo...")

def alimentar():
    print("Alimentando...")

funciones = [explotar, encender, alimentar]

def getFuncionRandom():
    return random.choice(funciones)

getFuncionRandom()()