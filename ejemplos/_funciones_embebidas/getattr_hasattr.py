class Calculadora:
    def __init__(self) -> None:
        self.fabricante = "Casio"
        self.__ns = "SN183478383"
    
    def calcular(self):
        print ("Calculando...")


c = Calculadora()
if (hasattr(c, "fabricante")):
    print(getattr(c,"fabricante"))
print(hasattr(c, "__ns"))
if (hasattr(c, "calcular")):
    getattr(c,"calcular")()