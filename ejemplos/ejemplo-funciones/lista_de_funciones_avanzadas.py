import time
def f1(x):
    print("Función 1")
    print("El resultado de multiplicar por 2 el parámetro es", x[0]*2)
    time.sleep(2)
def f2(x):
    print("Función 2")
    print(x[1],"tiene una calificación de",x[0])
    time.sleep(1)
def f3():
    print("Función 3")
    time.sleep(1)

diccionario_funciones = {f3:[],f2:[3,"Raúl"],f1:[2]}

for k,v in diccionario_funciones.items():
    if (len(v))==0:
        k()
    else:
        k(v)