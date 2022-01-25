from GestorPersistencia import GestorPersistencia
from FactoryPersistencia import FactoryPersistencia

#dato = "El dato"
#dato = 3
dato = 4.5

gp = FactoryPersistencia.get_sistema_persistencia(dato)
if (isinstance(gp, GestorPersistencia)):
    gp.guardar_dato(dato)
else:
    print("La instancia devuelta por el factory no es un Gestor de Persistencia válido")

