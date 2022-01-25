class CalculadoraMetaclase(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'sumar') and 
            callable(subclass.sumar) and 
            hasattr(subclass, 'restar') and 
            callable(subclass.restar)
        )
class ICalculadora(metaclass=CalculadoraMetaclase):
    pass
class Calculadora(ICalculadora):
    def sumar(self, s1, s2):
        print("Sumando...")
    def restar(self, s1, s2):
        print("Restando...")
c = Calculadora()
if (issubclass(c, ICalculadora)):
    print("OK, es una implementación.")
else:
    print("KO")
