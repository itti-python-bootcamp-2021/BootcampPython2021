numero = [1, -8, 10, 15]
no = sorted(numero)
print(no)

palabras = ["módulo","clase","atributo"]
po = sorted(palabras)
print(po)

def calcular_size(palabra):
    return (len(palabra))

po2 = sorted(palabras, key=calcular_size)
print(po2)

class Ordenador:
    def __init__(self, speed, ram) -> None:
        self.speed = speed
        self.ram = ram
    def __str__(self) -> str:
        return str(self.speed) + ":" + str(self.ram)
    
    @classmethod
    def calcular_porvelocidad(cls, ordenador):
        return ordenador.speed

    @classmethod
    def calcular_pormemoria(cls, ordenador):
        return ordenador.ram

o1 = Ordenador(2000,64)
o2 = Ordenador(1500,128)
o3 = Ordenador(800,256)
ordenadores = [o1,o2,o3]
oo = sorted(ordenadores, key=Ordenador.calcular_porvelocidad)
for o in oo:
    print(o)


