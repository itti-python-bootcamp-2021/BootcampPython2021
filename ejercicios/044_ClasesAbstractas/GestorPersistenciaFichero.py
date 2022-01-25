from GestorPersistencia import GestorPersistencia

class GestorPersistenciaFichero(GestorPersistencia):
    def guardar_dato(self, dato):
        print (f"Guardando {dato} en fichero")