class Persona:
    def andar(self):
        print("Soy Persona y estoy andando...")
    def comer(self):
        print("Soy Persona y estoy comiendo...")

class Programador(Persona):
    def programar(self):
        print("Soy Programador y estoy programando...")

class Alpinista(Persona):
    def andar(self):
        print("Soy Alpinista y estoy andando...")
    def escalar(self):
        print("Soy Alpinista y estoy escalando...")

class Ciclista(Persona):
    def andar(self):
        print("Soy Ciclista y estoy andando...")
    def montar_en_bici(self):
        print("Soy Ciclista y estoy montando en bici...")

class ProgramadorDeportista(Programador, Alpinista, Ciclista):
    def descansar(self):
        print("Soy Programador Deportista y estoy descansando...")

pd = ProgramadorDeportista()
pd.montar_en_bici()
pd.escalar()
pd.programar()
pd.comer()
pd.descansar()
pd.andar()