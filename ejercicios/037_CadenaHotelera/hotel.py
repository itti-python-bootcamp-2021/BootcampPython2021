class Hotel:
    def __init__(self, nombre, estrellas, ciudad) -> None:
        self.__nombre = nombre
        self.__estrellas = estrellas
        self.__ciudad = ciudad
        self.__habitaciones = []

    def get_habitaciones_minibar(self) -> list:
        habitaciones_con_minibar = []
        for habitacion in self.__habitaciones:
            if (habitacion.get_minibar()==True):
                habitaciones_con_minibar.append(habitacion)
        return habitaciones_con_minibar

    def add_habitacion(self, habitacion):
        self.__habitaciones.append(habitacion)

    #Destructor
    def __del__(self):
        print("Destruyendo el hotel")