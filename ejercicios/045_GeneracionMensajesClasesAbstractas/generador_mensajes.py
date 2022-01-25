from abc import ABC, abstractmethod

class GeneradorMensajes(ABC):
    @abstractmethod
    def obtener_mensaje(self, codigo_mensaje) -> str:
        pass