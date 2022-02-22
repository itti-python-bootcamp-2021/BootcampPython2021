def generador_datos():
    for dato in range(500_000_000):
        if (dato%100_000_000==0):
            print("Modulo:",dato)
        yield dato

total = 0
for elemento in generador_datos():
    total = total + elemento
print(total)

#Obtención de las primeras ejecuciones del generador
print("OBTENCIÓN PASO A PASO")
generador = generador_datos()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
