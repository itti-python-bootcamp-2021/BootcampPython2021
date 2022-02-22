import datetime
import sys
NUMERO_ELEMENTOS = 1_000_000

class Factura:
    def __init__(self) -> None:
        self.numero = 1000
        self.fecha = datetime.datetime(2020, 2, 28)
        self.nombre_cliente = "Sociedad Anónima, S.A."
        self.importe = 2_000.38

def get_facturas():
    facturas=[]
    for factura in range(NUMERO_ELEMENTOS):
        facturas.append(Factura())
    return facturas

for factura in get_facturas():
    pass

def get_facturas_generador():
    for factura in range(NUMERO_ELEMENTOS):
        yield Factura()

for i in get_facturas_generador():
    pass

print(sys.getsizeof(get_facturas()))
print(sys.getsizeof(Factura()))