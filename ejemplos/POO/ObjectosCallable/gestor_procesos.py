class GeneradorNominas:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def __call__(self):
        print("Generando la nómina de " + self.nombre)
        return True

class ImpresoraNominas:
    def __call__(self):
        print("Imprimir la nomina")
        return True

p1 = GeneradorNominas("Fernando")
p2 = ImpresoraNominas()
p3 = "Proceso 3"
procesos = [p1, p2, p3]
for p in procesos:
    if (callable(p)):
        p()