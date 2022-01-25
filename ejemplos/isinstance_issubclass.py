class GestorPersistencia(object):
    def saludar(self):
        print("Saludo de GP")
    def despedir(self):
        print("Despedida de GP")

class GestorPersistenciaCloud(GestorPersistencia):
    def saludar(self):
        super().saludar()
        print("Saludo de GPC")

gp = GestorPersistencia()
gpc = GestorPersistenciaCloud()
gpc.saludar()

#print(isinstance(gp, object))#True
#print(isinstance(gp, GestorPersistencia))#True
#print(isinstance(gp, GestorPersistenciaCloud))#False

#print(isinstance(gpc, object))#True
#print(isinstance(gpc, GestorPersistencia))#True
#print(isinstance(gpc, GestorPersistenciaCloud))#True

#print(issubclass(GestorPersistencia, object))#True
#print(issubclass(GestorPersistencia, GestorPersistencia))#True
#print(issubclass(GestorPersistencia, GestorPersistenciaCloud))#False
#print(issubclass(GestorPersistenciaCloud, object))#True
#print(issubclass(GestorPersistenciaCloud, GestorPersistencia))#True
#print(issubclass(GestorPersistenciaCloud, GestorPersistenciaCloud))#True
