import time
def f1():
    print("Función 1")
    time.sleep(2)
def f2():
    print("Función 2")
    time.sleep(1)
def f3():
    print("Función 3")
    time.sleep(1)
def f4():
    print("Función 4")
    time.sleep(4)
def nueva():
    print("Nueva")
    time.sleep(2)
def formatear_disco_duro():
    print("Formateando disco duro...")

lista_funciones = [f1,formatear_disco_duro, f2,f3,f4]

while (len(lista_funciones)>0):
    #funcion_a_ejecutar = lista_funciones.pop()() #Es lo mismo que las dos líneas de debajo
    funcion_a_ejecutar = lista_funciones.pop()
    funcion_a_ejecutar()
    lista_funciones.insert(0,nueva)