class Humano:
    def __init__(self, nombre, sexo, altura):
        #Atributos públicos
        self.nombre = nombre 
        self.altura = altura
        #Atributos privados
        self.__sexo = sexo

    #Método público
    def calcular_power(self):
        return len(self.nombre) + self.__calcular_power_personal()

    #Método privado 
    def __calcular_power_personal(self):
        return (self.altura*2)

    #Método público que accede a un método privado de otra instancia de la misma clase
    def calcular_superpowerotro(self, otro):
        return (otro.__calcular_power_personal())

victor = Humano("Víctor","Varón",175)
print(victor.nombre)
#print(victor.__sexo)#No nos permite acceder por ser privado
print(victor.calcular_power())
#print(victor.__calcular_power_personal())#No nos permite acceder por ser privado

#El método privado es accesible para cualquier instancia de la misma clase
fernando = Humano("Fernando","Varón",170)
print(fernando.calcular_superpowerotro(victor))

