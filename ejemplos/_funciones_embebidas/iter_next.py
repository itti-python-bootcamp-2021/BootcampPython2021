class Contabilidad:
    def __init__(self, facturas=[]):
        self.facturas = facturas
        self.indice_actual = 0
        self.incremento = 1

    def add_factura(self, factura):
        self.facturas.append(factura)

    def __next__(self):
        if (self.indice_actual==len(self.facturas)):
            raise StopIteration
        actual = self.facturas[self.indice_actual]
        self.indice_actual+=self.incremento
        return actual

    def __call__(self):
        return self.__next__()

class Factura:
    def __init__(self, cliente, importe) -> None:
        self.cliente = cliente
        self.importe = importe

    def __str__(self) -> str:
        return (f"{self.cliente} : {self.importe}")

f1 = Factura("Cliente 1", 100)
f2 = Factura("Cliente 2", 200)
f3 = Factura("Cliente 3", 300)
facturas = [f1,f2,f3]

#next(facturas) #TypeError 'list' object is not an iterator

#Iterador de Contabilidad
"""
contabilidad = Contabilidad(facturas)
while True:
    try:
        f = next(contabilidad)
        print(f)
    except StopIteration:
        break
"""

#Iterador de Facturas sin centinela
"""
print("***Sin centinela***")
iter_facturas = iter(facturas) #Facturas es una lista o tupla
while (True):
    try:
        factura = next(iter_facturas)
        print(factura)
    except StopIteration:
        break
"""

#Iterador de Contabilidad con centinela (provoca la detención del iterador)
"""
print("***Con centinela***")
contabilidad = Contabilidad(facturas)
iter_facturas = iter(contabilidad, f3) #contabilidad debe ser CALLABLE, F2 es el centinela
while (True):
    try:
        factura = next(iter_facturas)
        print(factura)
    except StopIteration:
        break
"""