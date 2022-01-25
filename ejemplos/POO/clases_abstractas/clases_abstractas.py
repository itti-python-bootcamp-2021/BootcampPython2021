from abc import ABC, abstractmethod
#Clase abstracta
class Tarificador(ABC):

    def obtener_datos_cliente(self):
        return "Datos del cliente"
    
    #Método abstracto
    @abstractmethod
    def calcular_tarifa(self):
        pass

    def calcular_factura(self):
        datos_cliente = self.obtener_datos_cliente()
        tarifa = self.calcular_tarifa()
        return tarifa * 10

class TarificadorElectrico(Tarificador):

    def calcular_tarifa(self):
        return 10

    

#t = Tarificador()#No se puede instanciar porque es una clase abstracta

te = TarificadorElectrico()
te.calcular_factura()