class Flota:
    def __init__(self, lista_vehiculos) -> None:
        self.lista_vehiculos = lista_vehiculos
        self.posicion = len(self.lista_vehiculos)

    def __iter__(self):
        return self

    def __next__(self):
        self.posicion-=1
        if self.posicion==-1:
            self.posicion=len(self.lista_vehiculos)-1
            raise StopIteration
        return self.lista_vehiculos[self.posicion]

flota = Flota(["Seat","Audi","Kia"])
for vehiculo in flota:
    print(vehiculo)