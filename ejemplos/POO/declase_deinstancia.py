class Humano:
    #Atributo de clase o estático (común a todas las instancias)
    familia = "Mamífero"
    def __init__(self, nombre, sexo, altura):
        #Atributos de instancia
        self.nombre = nombre
        self.sexo = sexo
        self.altura = altura

    #Método de clase o estáticos (El comportamiento es exáctamente igual para todos los objetos)
    @classmethod
    def calcular_power_general(cls):
        #Estas dos notaciones son la misma
        return len(cls.familia)
        #return len(Humano.familia)

    #Método de instancia
    def calcular_power(self):
        return len(Humano.familia) + len(self.nombre) + self.altura

mohamed = Humano("Mohamed","Varon",170)
fernando = Humano("Fernando","Varon",170)

#Acceso a atributos y métodos de instancia
print(mohamed.nombre)
print(mohamed.calcular_power())
print("POWER GENERAL:", Humano.calcular_power_general())

#Acceso a atributo de clase
print(Humano.familia)
Humano.familia="Animal"
print(fernando.familia)


