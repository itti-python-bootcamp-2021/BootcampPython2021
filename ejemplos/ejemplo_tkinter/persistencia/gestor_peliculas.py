import sqlite3

from model.pelicula import Pelicula

class GestorBBDD:
    # Atributos
    DATABASE_NAME = "./datos/base_de_datos_oo.db"
    connection = None

    # Constructor
    def __init__(self):
        print("Ejecutando el constructor...")
        self.connection = sqlite3.connect(self.DATABASE_NAME)

    # Destructor
    def __del__(self):
        print("Ejecutando el destructor...")
        self.connection.close()

    # Métodos
    def crear_esquema_normal(self):
        cursor = self.connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, director TEXT NOT NULL, anyo INTEGER NOT NULL)"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def create(self, pelicula):
        cursor = self.connection.cursor()
        sql = f"INSERT INTO peliculas (titulo, director, anyo) VALUES ('{pelicula.titulo}', '{pelicula.director}', {pelicula.anyo})"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()
        
    def findAll(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM peliculas"
        lista_peliculas = cursor.execute(sql).fetchall()
        cursor.close()
        return lista_peliculas

    def findById(self, id):
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM peliculas where id={id}"
        registro = cursor.execute(sql).fetchone()
        pelicula = Pelicula(registro[0],registro[1],registro[2],registro[3],None)
        cursor.close()
        return pelicula

    def delete(self, id):
        cursor = self.connection.cursor()
        sql = f"DELETE FROM peliculas where id={id}"
        print(sql)
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def update(self, pelicula):
        cursor = self.connection.cursor()
        sql = f"UPDATE peliculas SET titulo='{pelicula.titulo}', director='{pelicula.director}', anyo={pelicula.anyo} WHERE id={pelicula.id}"
        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

