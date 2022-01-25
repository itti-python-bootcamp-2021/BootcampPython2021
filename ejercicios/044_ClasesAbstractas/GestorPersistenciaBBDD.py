from GestorPersistencia import GestorPersistencia

class GestorPersistenciaBBDD(GestorPersistencia):
    def guardar_dato(self, dato):
        print (f"Guardando {dato} en base de datos")