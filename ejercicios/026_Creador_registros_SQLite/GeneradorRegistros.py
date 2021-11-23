import random
import sqlite3
import time

NUMERO_INDIVIDUOS = 10000
EDAD_MINIMA = 1
EDAD_MAXIMA = 100
DATABASE_NAME = "clientes.db"

nombres = ["Juan Luis","Luis","Alejandra","Ricardo","Virginia","Fernando"]
apellidos = ["Roca", "Viadero", "Aceves", "Ruiz", "Bota", "Paniagua"]

edades = [random.randint(EDAD_MINIMA,EDAD_MAXIMA) for i in range(NUMERO_INDIVIDUOS)]
personas = [(random.choice(nombres) + " " + random.choice(apellidos) + " " + 
    random.choice(apellidos)) for i in range(NUMERO_INDIVIDUOS)]

#INSERTAR LOS n REGISTROS EN LA BASE DE DATOS.
#Crear la base de datos.
#Crear el esquema: tabla PERSONAS (id, nombre, edad).
#Insertar todos las personas.

def open_connection(database_name):
    global connection
    connection = sqlite3.connect(database_name)

def close_connection():
    connection.close()

def create_squema():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, edad INTEGER NOT NULL)")
    connection.commit()
    cursor.close()

def insertar_persona(nombre, edad):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO clientes (nombre, edad) VALUES ('{nombre}',{edad})")
    connection.commit()
    cursor.close()

def insertar_personas(lista_personas):
    cursor = connection.cursor()
    for personas in lista_personas:
        cursor.execute(f"INSERT INTO clientes (nombre, edad) VALUES ('{personas[0]}',{personas[1]})")
    connection.commit()
    cursor.close()

def insertar_personas_execute_many(lista_personas):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO clientes (nombre, edad) VALUES (?,?)",lista_personas)
    connection.commit()
    cursor.close()

def delete_all_personas():
    cursor = connection.cursor()
    cursor.execute("DELETE FROM clientes")
    connection.commit()
    cursor.close()

def inicializar_cronometro():
    return time.time()*1000

def finalizar_cronometro(inicial):
    return (time.time()*1000-inicial)/1000

open_connection(DATABASE_NAME)
#create_squema()
#Tenemos dos listas: edades y personas

#OPCION 1
delete_all_personas()
inicio = inicializar_cronometro()
for i in range(0,len(personas)):
    insertar_persona(personas[i],edades[i])
print("Opción 1: Tiempo total (segundos):" + str(finalizar_cronometro(inicio)))

#OPCION 2
delete_all_personas()
inicio = inicializar_cronometro()
lista_clientes = list(zip(personas, edades))
for cliente in lista_clientes:
    insertar_persona(cliente[0],cliente[1])
print("Opción 2: Tiempo total (segundos):" + str(finalizar_cronometro(inicio)))

#OPCION 3
delete_all_personas()
inicio = inicializar_cronometro()
lista_clientes = list(zip(personas, edades))
insertar_personas(lista_clientes)
print("Opción 3: Tiempo total (segundos):" + str(finalizar_cronometro(inicio)))

#OPCION 4
delete_all_personas()
inicio = inicializar_cronometro()
lista_clientes = list(zip(personas, edades))
insertar_personas_execute_many(lista_clientes)
print("Opción 4: Tiempo total (segundos):" + str(finalizar_cronometro(inicio)))

close_connection()