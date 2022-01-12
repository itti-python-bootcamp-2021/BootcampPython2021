from hotel import Hotel
from habitacion import Habitacion

class CadenaHotelera:
    #Constructor
    def __init__(self, nombre, anyo_fundacion, sede_social="Barcelona") -> None:
        self.__nombre = nombre
        self.__anyo_fundacion = anyo_fundacion
        self.__sede_social = sede_social
        self.__hoteles = []
        self.__anyo = 1999

    def get_habitaciones_minibar(self):
        hoteles_con_minibar = []
        for hotel in self.__hoteles:
            hoteles_con_minibar += hotel.get_habitaciones_minibar()
        return hoteles_con_minibar

    def add_hotel(self, hotel):
        self.__hoteles.append(hotel)

    #Destructor
    def __del__(self):
        print("Destruyendo la cadena hotelera")

if __name__ == "__main__":
    #Instanciación
    melia = CadenaHotelera("Melia",1998)

    hotel1 = Hotel("Melia Ciudad de Barcelona",5,"Barcelona")
    hotel2 = Hotel("Melia Castilla",5,"Madrid")
    hotel3 = Hotel("Melia Princesa",5,"Madrid")

    melia.add_hotel(hotel1)
    melia.add_hotel(hotel2)
    melia.add_hotel(hotel3)

    h1 = Habitacion(100,2,True,False)
    h2 = Habitacion(101,1,False)
    h3 = Habitacion(100,2,False)
    h4 = Habitacion(101,2,True,False)
    h5 = Habitacion(23,4,False)
    h6 = Habitacion(27,2,True)

    hotel1.add_habitacion(h1)
    hotel1.add_habitacion(h2)
    hotel2.add_habitacion(h3)
    hotel2.add_habitacion(h4)
    hotel3.add_habitacion(h5)
    hotel3.add_habitacion(h6)
    
    hb = melia.get_habitaciones_minibar()
    for h in hb:
        print(h.get_numero())