class Alimento:
    def __init__(self, nombre, precio):
        self.__nombre = nombre #¿Privado?
        self.precio = precio #Público
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        if (nombre=="xxxx"):
            raise Exception
        self.__nombre = nombre
    def set_precio(self, precio):
        self.precio = precio
    #Método público
    def calcular_cuadruple(self, numero):
        resultado = self.__calcular_doble(numero)*2
        return resultado
    #Método ¿privado?
    def __calcular_doble(self, numero):
        return numero * 2

    

pan = Alimento("Pan",5)
#pan.set_nombre("Panecillo")
pan._Alimento__nombre = "Panecillo"
print(pan.get_nombre())
print(pan.precio)
print(pan._Alimento__calcular_doble(10))



#print(pan.get_nombre())