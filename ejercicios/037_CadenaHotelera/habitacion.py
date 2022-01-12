class Habitacion:
    def __init__(self, numero, capacidad, minibar, disponible=True) -> None:
        self.__numero = numero
        self.__capacidad = capacidad
        self.__minibar = minibar
        self.__disponible = disponible

    def get_minibar(self):
        return self.__minibar

    def get_numero(self):
        return self.__numero

    def set_minibar(self, minibar):
        self.__minibar = minibar

    #Destructor
    def __del__(self):
        print("Destruyendo la habitacion")