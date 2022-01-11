class Habitacion:
    def __init__(self, numero, capacidad, minibar, disponible=True) -> None:
        self.numero = numero
        self.capacidad = capacidad
        self.minibar = minibar
        self.disponible = disponible

