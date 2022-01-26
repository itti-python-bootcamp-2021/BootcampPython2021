class Factura:
    def __init__(self, importe, fecha) -> None:
        print("EN EL INIT")
        self.importe = importe
        self.fecha = fecha

    def __add__(self, otra_factura):
        return self.importe + otra_factura.importe

    def __sub__(self, otra_factura):
        return self.importe - otra_factura.importe

    def __mul__(self, otra_factura):
        return self.importe * otra_factura.importe

    def __truediv__(self, otra_factura):
        return self.importe / otra_factura.importe

f1 = Factura(100,"15/05/2021")
f2 = Factura(25,"14/05/2021")
print(f1+f2)