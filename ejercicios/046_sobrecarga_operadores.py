"""
Sobreescritura de los métodos __lt__ y __gt__ para sobrecargar los
operadores < y >.
Empleado1 > Empleado2 si:
- La categoria de E1 > la de E2
- Si las categorías son iguales, si salario de E1 > el de E2
- Si los salarios son iguales, si antiguedad de E1 > la de E2

"""
from operator import truediv


class Empleado:
    def __init__(self, nombre, categoria, salario, antiguedad):
        self.nombre = nombre
        self.categoria = categoria
        self.salario = salario
        self.antiguedad = antiguedad

    def __eq__(self, other):
        return (self.categoria==other.categoria) and (self.salario==other.salario) and (self.antiguedad==other.antiguedad)

    def __gt__(self, other):
        if (self.__eq__(other)):
            return False

        if (self.categoria>other.categoria):
            return True
        elif (self.categoria<other.categoria):
            return False

        if (self.salario>other.salario):
            return True
        elif (self.salario<other.salario):
            return False
        
        if (self.antiguedad>other.antiguedad):
            return True
        elif (self.antiguedad<other.antiguedad):
            return False

    def __lt__(self, other):
        if (self.__eq__(other)):
            return False

        return not self.__gt__(other)

empleado1 = Empleado("Manuel", 5,50000,3)
empleado2 = Empleado("Adriana", 6,50000,3)
print(empleado1<empleado2)