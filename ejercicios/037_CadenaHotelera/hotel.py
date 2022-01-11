class Hotel:
    def __init__(self, nombre, estrellas, ciudad) -> None:
        self.nombre = nombre
        self.estrellas = estrellas
        self.ciudad = ciudad
        self.habitaciones = []

    def get_habitaciones_minibar(self):
        habitaciones_con_minibar = []
        for habitacion in self.habitaciones:
            if (habitacion.minibar==True):
                habitaciones_con_minibar.append(habitacion)
        return habitaciones_con_minibar