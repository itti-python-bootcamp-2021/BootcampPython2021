class Equipo:
    def __init__(self, nombre, presupuesto, deuda):
        self.nombre = nombre
        self._presupuesto = presupuesto
        self.__deuda = deuda
    #Getter - Método de acceso
    def get_deuda(self):
        return self.__deuda

    #Setter - Método de acceso
    def set_deuda(self, nueva_deuda):
        self.__deuda = nueva_deuda

    #Getter - Con el decorador @property
    @property
    def deuda(self):
        return self.__deuda

    #Setter - Con el decorador setter
    @deuda.setter
    def deuda(self, nueva_deuda):
        self.__deuda = nueva_deuda

    #Getter - Con el decorador @property
    @property
    def presupuesto(self):
        return self._presupuesto

    #Setter - Con el decorador setter
    @presupuesto.setter
    def presupuesto(self, nuevo_presupuesto):
        self._presupuesto = nuevo_presupuesto
    
fc_elche = Equipo("F.C. Elche", 1000000, 20000)

#Acceso de modificación al atributo público
fc_elche.nombre = "Elche F.C."
#Acceso de escritura al atributo privado
#--Por método setter
fc_elche.set_deuda(12000)
#--Con un decorador setter
#fc_elche.deuda = 15000

#Acceso de lectura al atributo público
print(fc_elche.nombre)
#Acceso de lectura al atributo privado
#--Por método getter
print(fc_elche.get_deuda())
#--Con un decorador @property
print(fc_elche.deuda)

fc_elche.presupuesto = 1200
print(fc_elche.presupuesto)