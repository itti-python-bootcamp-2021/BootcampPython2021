from GestorPersistencia import GestorPersistencia

class GestorPersistenciaCloud(GestorPersistencia):
    def guardar_dato(self, dato):
        print (f"Guardando {dato} en la nube")