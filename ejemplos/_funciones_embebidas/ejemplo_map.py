class Factura:
    IVA = 0.21
    def __init__(self, cliente, importe) -> None:
        self.cliente = cliente
        self.importe = importe
        self.iva = None
    
    @classmethod
    def calcular_impuestos(cls, factura):
        print("Calculando impuestos...")
        factura.iva = factura.importe * cls.IVA
        return factura

f1 = Factura("Cliente 1", 100)
f2 = Factura("Cliente 2", 200)
f3 = Factura("Cliente 3", 300)
facturas = [f1,f2,f3]

facturas_coniva = list(map(Factura.calcular_impuestos, facturas))

for f in facturas_coniva:
    print (f.cliente, f.importe, f.iva)
