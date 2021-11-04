contador=0
numeros = [8,3,10,35,1,20,5]
#numeros = [1,2,3,4,5,6,7]
for j in range(0,len(numeros)):
    for i in range(0,len(numeros)-1):
        contador+=1
        if numeros[i]>numeros[i+1]:
            numeros[i],numeros[i+1]=numeros[i+1],numeros[i]
print(numeros)
print("He necesitado",contador,"iteracciones")