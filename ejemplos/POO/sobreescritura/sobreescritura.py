class Animal:
    def comer(self):
        print("Comiendo como animal")
    def dormir(self):
        print("Durmiendo como animal")


class Reptil(Animal):
    def dormir(self): #Sobreescritura
        print("Durmiendo como reptil")

class Ave(Animal):
    def dormir(self): #Sobreescritura
        super().dormir()
        print("Además duermiendo como ave")


Reptil().dormir()
Ave().dormir()