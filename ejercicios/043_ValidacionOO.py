"""
Clase: Producto
Atributos:
    - Nombre (No puede estar vacío ni estar compuesto por espacios en blanco)
    - PVP (No puede ser 0 ni negativo)
    - Categoría (Tiene que ser un elemento de la tupla (Informática, Textil, Jardín))

Método:
    - get_pvp-->Devuelve el precio de venta al público.

Clase: ProductoRebajado(Producto)
    - Descuento (No puede ser 0 o negativo ni mayor de 90%)
    - get_pvp-->Devuelve el precio de venta al público con el descuento. Hay que utilizar el método get_pvp del padre.

NOTA: Se genera un excepcion que contiene una lista de excepciones para propagar todos los errores.
"""
class ProductoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.errores = []
    def add_error(self, error):
        self.errores.append(error)

class Producto(object):
    categorias = ("Informática", "Textil", "Jardín") #Atributo de clase (estático)
    def __init__(self, nombre : str, pvp : int, categoria : str) -> None:
        super().__init__()
        productoException = ProductoException()
        if (nombre.strip()==""):
            productoException.add_error(ValueError("El nombre no puede estar vacío ni contener solo espacios"))
        if (pvp<=0):
            productoException.add_error(ValueError("El PVP no puede ser 0 ni negativo"))
        if (categoria not in Producto.categorias):
            productoException.add_error(ValueError("La categoría no es de las aceptadas"))
        if (len(productoException.errores)>0):
            raise productoException
        self.nombre = nombre
        self.pvp = pvp
        self.categoria = categoria
    def get_pvp(self):
        return self.pvp

class ProductoRebajado(Producto):
    def __init__(self, nombre: str, pvp: int, categoria: str, descuento : int) -> None:
        super().__init__(nombre, pvp, categoria)
        self.descuento = descuento
    def get_pvp(self):#Sobreescritura
        #Observen que los dos métodos get_pvp de la clase base y de la clase heredad conviven
        return super().get_pvp()-(super().get_pvp()*(1/self.descuento))

try:
    p = ProductoRebajado("PC",1000.0,"Informática",10.0)
    print(p.get_pvp())
except ProductoException as e:
    for error in e.errores:
            print(error)
except Exception as e:
    print(e)