class Jefe:
    def calcular_salario(self, subordinado):
        print(len(subordinado.__nombre())*1000)#ERROR

class Subordinado:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    def calcular_diferencia(self, otro):
        print( (len(self.__nombre)*1000) - (len(otro.__nombre)*1000) )

empleado1=Subordinado("Blas")
empleado2=Subordinado("Nabucodonsor")
empleado1.calcular_diferencia(empleado2)
#jefe1=Jefe()
#jefe1.calcular_salario(empleado1)#PRODUCE UN ERROR

