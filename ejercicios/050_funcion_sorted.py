"""
Crear la clase Cliente con los atributos nombre, facturacion_anual y deuda_pendiente_anual
Crear 3 clientes y ordenar según el siguiente algoritmo:
    facturacion_anual - deuda_pendiente_anual
"""
class Cliente:
    def __init__(self,nombre,facturacion_anual,deuda_pendiente_anual) -> None:
        self.nombre=nombre
        self.facturacion_anual=facturacion_anual
        self.deuda_pendiente_anual=deuda_pendiente_anual

    @classmethod
    def ordenar(cls,cliente):
        return cliente.facturacion_anual - cliente.deuda_pendiente_anual

    def __str__(self) -> str:
        return self.nombre

c1=Cliente("Juan Luis",10000,2000)
c2=Cliente("Fernando",1000,500)
c3=Cliente("Victor",15000,10000)        

clientes=[c1,c2,c3]
clt=sorted(clientes,key=Cliente.ordenar)
for c in clt:
    print(c)
