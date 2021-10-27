#break, continue
nombres = ["Arantzazu","Alejandra","Ramón","Almudena","Ramón","Alejandra","Julián"]
nombre_buscado = input("Dime un nombre:")
print("USANDO BREAK...")
for nombre in nombres:
    print("Evaluando",nombre)
    if (nombre_buscado==nombre):
        print("¡Lo encontré!")
        break #Sale del bucle

print("USANDO CONTINUE...")

for nombre in nombres:
    print("Evaluando",nombre)
    if (nombre_buscado==nombre):
        print("¡Lo encontré!")
        continue #Sale de la iteracción pero sigue con el siguiente elemento
    print("Haciendo un proceso que tarda un rato en ejecutarse...")

