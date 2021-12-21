import sqlite3
DATABASE_NAME = "base_de_datos.db"
connection = None
def establecer_conexion():
    print("Estableciendo la conexión...")
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def cerrar_conexion(connection):
    print("Cerrando la conexión...")
    connection.close()

def crear_esquema_normal():
    print("Creando esquema...")
    cursor = connection.cursor()
    sql="CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, edad INTEGER NOT NULL)"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

def crear_esquema_automatico(nombre_tabla, columnas):
    print("Creando esquema...")
    cursor = connection.cursor()
    primera_columna=True
    sql=f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ("
    for columna in columnas:
        if (not primera_columna):
            sql+=", "
        else:
            primera_columna=False
        sql+=columna["NAME"]+" "+columna["TYPE"]
        if (columna["PK"]==True):
            sql+=" PRIMARY KEY"
        if (columna["AI"]==True):
            sql+=" AUTOINCREMENT"
        if (columna["NOT_NULL"]==True):
            sql+=" NOT NULL"
    sql+=")"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

connection = establecer_conexion()
crear_esquema_normal()
"""
columna1 = {"NAME":"id","TYPE":"INTEGER","PK":True,"AI":True,"NOT_NULL":False}
columna2 = {"NAME":"nombre","TYPE":"TEXT","PK":False,"AI":False,"NOT_NULL":True}
columna3 = {"NAME":"edad","TYPE":"INTEGER","PK":False,"AI":False,"NOT_NULL":True}
columnas = (columna1,columna2,columna3)
crear_esquema_automatico("clientes",columnas)
"""
cerrar_conexion(connection)