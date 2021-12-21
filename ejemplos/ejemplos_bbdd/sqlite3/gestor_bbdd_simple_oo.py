import sqlite3
from clase_columna import ColumnaDB

class GestorBBDD:
    # Atributos
    database_name = None
    connection = None

    # Constructor
    def __init__(self, database_name):
        print("Ejecutando el constructor...")
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)

    # Destructor
    def __del__(self):
        print("Ejecutando el destructor...")
        self.connection.close()

    # Métodos
    def crear_esquema_normal(self):
        cursor = self.connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, edad INTEGER NOT NULL)"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def crear_esquema_automatico(self, nombre_tabla, columnas):
        print("Creando esquema...")
        cursor = self.connection.cursor()
        primera_columna = True
        sql = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ("
        for columna in columnas:
            if not primera_columna:
                sql += ", "
            else:
                primera_columna = False
            sql += columna.name + " " + columna.type
            if columna.pk == True:
                sql += " PRIMARY KEY"
            if columna.ai == True:
                sql += " AUTOINCREMENT"
            if columna.not_null == True:
                sql += " NOT NULL"
        sql += ")"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

gestor = GestorBBDD("base_de_datos_oo.db")
gestor.crear_esquema_normal()

"""
columna1 = ColumnaDB("id", "INTEGER", True, True, False)
columna2 = ColumnaDB("nombre", "TEXT", False, False, True)
columna3 = ColumnaDB("edad", "INTEGER", False, False, True)
columnas = (columna1, columna2, columna3)
gestor.crear_esquema_automatico("clientes", columnas)
"""