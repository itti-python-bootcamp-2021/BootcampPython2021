from abc import ABC, abstractmethod

class GestorPersistencia(ABC):
    def __init__(self):
        print("Iniciando gestor de persistencia...")
        self.version = "1.0"

    @abstractmethod
    def guardar_dato(self, dato):
        pass

    def mostrar_version(self):
        print(self.version)


