class Vehiculo:
    def __init__(self, nombre, velocidad_maxima, numero_serie) -> None:
        self.nombre = nombre #Público
        self._velocidad_maxima = velocidad_maxima #Protected
        self.__numero_serie = numero_serie #Privado

class Avion(Vehiculo):
    def __init__(self, nombre, velocidad_maxima, numero_serie) -> None:
        super().__init__(nombre, velocidad_maxima, numero_serie)
    def mostrar_atributos(self):
        print(self.nombre)
        print(self._velocidad_maxima)
        #print(self.__numero_serie)#ERROR

class Barco():
    def mostrar_atributos_otro(self, vehiculo):
        print(vehiculo.nombre)#OK
        print(vehiculo._velocidad_maxima)
        #print(vehiculo.__numero_serie)#KO

f18 = Avion("F18",5000,"SN123456")
#f18.mostrar_atributos()
barco = Barco()
barco.mostrar_atributos_otro(f18)