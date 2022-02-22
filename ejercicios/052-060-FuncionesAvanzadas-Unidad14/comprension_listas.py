#Crear con comprensión de listas una lista en la que aparezcan de los números entre
#1 y 100, los valores true o false si el número es par (true) o no (false).
#1,2,3,4 --> [false, true, false, true...]
def es_par(numero):
    return numero%2==0
lista = [es_par(x) for x in range(1,101)]
print(lista)

#Crear una lista con los números pares comprendidos entre el 1 y el 100.
lista = [x for x in range(1,101) if x%2==0]
print(lista)

#Crear una lista con los números del rango [1-100] sustituyendo los impares por 'IMPAR'
lista = [x if x%2==0 else "IMPAR" for x in range(1,101)]
print(lista)

#Crear una lista con los números del rango [1-100] que sean mayores de 
# 50 sustituyendo los impares por 'IMPAR'
def decisor(numero):
    return("IMPAR")
lista = [x if x%2==0 else decisor(x) for x in range(1,101) if x>50]
print(lista)

#Crear un conjunto con los números del rango [1-100] sustituyendo los impares por 'IMPAR'
conjunto = {x if x%2==0 else "IMPAR" for x in range(1,101)}
print(conjunto)

#Crear un diccionario con los números del rango [1-100] como clave y como valor PAR o IMPAR
diccionario = {x:es_par(x) for x in range(1,101)}
print(diccionario)

"""
Suponemos que tenemos una estructura de datos con las traducciones de ciertas palabras entre
inglés y castellano.
"""
diccionario_en_es = (("Home","Casa"),("Dog","Perro"),("Sunflower","Girasol"),("Beach","Playa"))
lista_inicial = ["Dog","Beach","Sunflower"]
#Dadas las estructuras de datos, crear un diccionario utilizando list-comprenhension con
#la palabra inicial como clave y la traducción como valor.
#Las funciones get_traduccion y get_traduccion_compacta son equivalentes. Solo haría falta una.
def get_traduccion(palabra):
    for traduccion in diccionario_en_es:
        if (traduccion[0]==palabra):
            return traduccion[1]
    return "Desconocido"

def get_traduccion_compacta(palabra):
    lista = [traduccion[1] for traduccion in diccionario_en_es if traduccion[0]==palabra]
    if len(lista)==0:
        lista.append("Desconocido")
    return(lista[0])

diccionario_traducciones = {palabra:get_traduccion(palabra) for palabra in lista_inicial}
print(diccionario_traducciones)

