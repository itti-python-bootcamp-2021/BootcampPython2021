from hotel import Hotel
from habitacion import Habitacion

class CadenaHotelera:
    def __init__(self, nombre, anyo_fundacion, sede_social) -> None:
        self.nombre = nombre
        self.anyo_fundacion = anyo_fundacion
        self.sede_social = sede_social
        self.hoteles = []

    def get_habitaciones_minibar(self):
        hoteles_con_minibar = []
        for hotel in self.hoteles:
            hoteles_con_minibar += hotel.get_habitaciones_minibar()
        return hoteles_con_minibar

if __name__ == "__main__":
    #Instanciación
    melia = CadenaHotelera("Melia",1998,"Barcelona")
    
    hotel1 = Hotel("Melia Ciudad de Barcelona",5,"Barcelona")
    hotel2 = Hotel("Melia Castilla",5,"Madrid")
    hotel3 = Hotel("Melia Princesa",5,"Madrid")

    melia.hoteles.append(hotel1)
    melia.hoteles.append(hotel2)
    melia.hoteles.append(hotel3)

    h1 = Habitacion(100,2,True,False)
    h2 = Habitacion(101,1,False)
    h3 = Habitacion(100,2,False)
    h4 = Habitacion(101,2,True,False)
    h5 = Habitacion(23,4,False)
    h6 = Habitacion(27,2,True)

    hotel1.habitaciones.append(h1)
    hotel1.habitaciones.append(h2)
    hotel2.habitaciones.append(h3)
    hotel2.habitaciones.append(h4)
    hotel3.habitaciones.append(h5)
    hotel3.habitaciones.append(h6)
    
    hb = melia.get_habitaciones_minibar()
    print(type(hb))
    for h in hb:
        print(h.numero)