class Flota:
    def __init__(self, lista) -> None:
        self.lista = lista
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if (self.index == len(self.lista)):
            raise StopIteration #Indica al iterador que debe parar
            #self.index=0#Lista circular
        return self.lista[self.index]

f = Flota(["Seat","Audi","Renault","Kia"])
for vehiculo in f:
    print(vehiculo)