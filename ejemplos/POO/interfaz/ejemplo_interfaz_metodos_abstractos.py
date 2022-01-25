from abc import ABC, abstractmethod
class ICalculadora(ABC):
    @abstractmethod
    def sumar(self):
        pass
    @abstractmethod
    def restar(self):
        pass

class CalculadoraDecimal(ICalculadora):
    def sumar(self):
        print("Sumando")
    def restar(self):
        pass

#Esta clase sería abstracta al no tener implementados todos los métodos abstractos
class CalculadoraErronea(ICalculadora):
    def sumar(self):
        print("Sumando...")

class CalculadoraFake():
    pass

def sumar(calculadora):
    if isinstance(calculadora, ICalculadora):
        calculadora.sumar()
    else:
        print("Error")

sumar(CalculadoraFake())#Error
sumar(CalculadoraDecimal())#OK
sumar(CalculadoraErronea())#Error