class Animal:
    def nacer(self):
        print("Naciendo...")
    def morir(self):
        print("Muriendo...")

class Volador(Animal):
    def volar(self):
        print("Volando...")

class Nadador(Animal):
    def nadar(self):
        print("Nadando...")

class Pato(Volador, Nadador):
    def patear(self):
        print("Cua-Cua...")

lucas = Pato()
lucas.nacer()
lucas.patear()
lucas.nadar()
lucas.volar()
lucas.morir()