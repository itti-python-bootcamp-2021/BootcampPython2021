#CLASE BASE, CLASE PADRE
class Animal:
    def __init__(self, nombre, familia) -> None:
        self.nombre = nombre
        self.familia = familia

    def comer(self):
        print(f"Soy {self.nombre} Comiendo (como un Animal)...")

    def dormir(self):
        print(f"Soy {self.nombre} Durmiendo (como un Animal)...")

#CLASE DERIVADA, CLASE HIJA
class Ave(Animal):
    def __init__(self, nombre, familia, impermeable):
        super().__init__(nombre, familia)
        self.impermeable = impermeable

    def volar(self):
        print(f"Soy {self.nombre} Volando...")

    #Sobreescritura de método
    def comer(self):
        print(f"Soy {self.nombre} Comiendo (como un ave)...")


#CLASE DERIVADA, CLASE HIJA
class Pez(Animal):
    def __init__(self, nombre, familia):
        super().__init__(nombre, familia)

    def nadar(self):
        print(f"Soy {self.nombre} Nadando...")

    #Sobreescritura con llamada a la versión del método de la clase base
    def dormir(self):
        super().dormir()#Ejecutando la versión de dormir de la clase base
        print(f"Soy {self.nombre} Durmiendo (como un Pez) (con los ojos abiertos)")

gallina = Ave("Gallina","Phasianidae", False)
sardina = Pez("Sardina","Clupeidae")
gallina.comer()
gallina.dormir()
gallina.volar()
sardina.nadar()
sardina.comer()
sardina.dormir()
