class Ciudad:
    poblacion_maxima = 200_000
    def __init__(self, nombre, poblacion) -> None:
        self.nombre = nombre
        self.__poblacion = poblacion

    @classmethod
    def duplicar_poblacion(cls):
        cls.poblacion_maxima = cls.poblacion_maxima * 2

    def get_capacidad_poblacion_pendiente(self):
        capacidad_poblacion_pendiente = Ciudad.poblacion_maxima - self.__poblacion
        return capacidad_poblacion_pendiente

    def __mostrar_capacidad_poblacion_pendiente(self):
        print(self.get_capacidad_poblacion_pendiente())

alcorcon = Ciudad("Alcorcón",177_000)
print(Ciudad.poblacion_maxima)#OK
print(alcorcon.nombre)#OK
#print(alcorcon.__poblacion)#KO
Ciudad.duplicar_poblacion()#OK
alcorcon.duplicar_poblacion()#OK
#Ciudad.get_capacidad_poblacion_pendiente()#KO
alcorcon.get_capacidad_poblacion_pendiente()#OK
#alcorcon.__mostrar_capacidad_poblacion_pendiente()#KO