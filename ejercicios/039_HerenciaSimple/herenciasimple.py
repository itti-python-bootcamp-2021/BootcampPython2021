class Vehiculo:
    def __init__(self, velocidad, peso) -> None:
        self.velocidad = velocidad
        self.peso = peso

    def avanzar(self):
        print("Avanzando...")

    def frenar(self):
        print("Frenando...")

class VehiculoTerrestre(Vehiculo):
    def __init__(self, velocidad, peso, numero_ruedas) -> None:
        super().__init__(velocidad, peso)
        self.numero_ruedas = numero_ruedas

    def cambiar_rueda(self):
        print("Cambiando rueda...")

class VehiculoAereo(Vehiculo):
    def __init__(self, velocidad, peso, altitud_maxima) -> None:
        super().__init__(velocidad, peso)
        self.altitud_maxima = altitud_maxima
    def volar(self):
        print("Volando...")

class VehiculoMaritimo(Vehiculo):
    def __init__(self, velocidad, peso, profundidad_minima) -> None:
        super().__init__(velocidad, peso)
        self.profundad_minima = profundidad_minima

    def navegar(self):
        print("Navegando...")

    def frenar(self):
        print("Frenando echando el ancla...")


vm = VehiculoMaritimo(100,200,10)
vm.avanzar()
vm.navegar()