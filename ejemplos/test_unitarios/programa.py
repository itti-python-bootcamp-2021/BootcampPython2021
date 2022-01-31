lista = ["uno","dos","cuatro"]

def get_lista():
    return lista

def esta_en_la_lista(elemento):
    return elemento in lista

def saludar():
    return "Hola"

def sumar(s1, s2):
    return s1+s2

def dividir(d1, d2):
    #ZeroDivisionError si d2 es 0
    if (d2==0):
        raise MiZeroException()
    return (d1/d2)

class MiZeroException(Exception):
    pass

class Animal:
    def __init__(self, nombre, numero_patas) -> None:
        self.nombre = nombre
        self.numero_patas = numero_patas
    def get_longitud(self):
        longitud = len(self.nombre)+self.numero_patas
        if (longitud%2==0):
            longitud+=1
        return longitud