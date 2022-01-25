class ICalculadora:
    def sumar(self, s1, s2):
        raise NotImplementedError
    def restar(self, s1, s2):
        raise NotImplementedError

class CalculadoraDecimal(ICalculadora):
    def sumar(self, s1, s2):
        return s1+s2
    def restar(self, s1, s2):
        return s1-s2

class CalculadoraOctal(ICalculadora):
    def sumar(self, s1, s2):
        return oct(int(str(s1), 8) + int(str(s2), 8))
    def restar(self, s1, s2):
        return oct(int(str(s1), 8) - int(str(s2), 8))

def get_calculadora(numero):
    if (numero==10):
        return CalculadoraDecimal()
    elif (numero==8):
        return CalculadoraOctal()

calculadora = get_calculadora(10)
if (isinstance(calculadora,ICalculadora)):
    calculadora.restar(10,2)
else:
    print("No es una calculadora")