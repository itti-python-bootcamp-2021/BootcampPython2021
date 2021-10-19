import time
print("---Bienvenido al temporizador---")
minutos = int(input("Introduce el número de minutos a contar:")) #Pedimos al usuario el tiempo de espera
segundos = minutos * 60
for i in range(segundos, 0, -1):
    print("Faltan",i,"segundos")
    time.sleep(1)