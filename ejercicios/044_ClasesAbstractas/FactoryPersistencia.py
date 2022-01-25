from GestorPersistencia import GestorPersistencia
from GestorPersistenciaFichero import GestorPersistenciaFichero
from GestorPersistenciaBBDD import GestorPersistenciaBBDD
from GestorPersistenciaCloud import GestorPersistenciaCloud

class FactoryPersistencia:
    @classmethod
    def get_sistema_persistencia(self, dato) -> GestorPersistencia:
        if (isinstance(dato, str)):
            gpf = GestorPersistenciaBBDD()
        elif (isinstance(dato, int)):
            gpf = GestorPersistenciaCloud()
        else:
            gpf = GestorPersistenciaFichero()
        return gpf