class Estaciones:
    def __init__(self):
        self.estaciones = ["Primavera","Verano","Otoño","Invierno"]
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__indice==len(self.estaciones)):
            raise StopIteration
        siguiente = self.estaciones[self.__indice]
        self.__indice=self.__indice+1
        return siguiente

e = Estaciones()
for x in e:
    print(x)