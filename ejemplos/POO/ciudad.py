from generador_pdfs import generar_pdf

class Ciudad:
    def __init__(self, nombre, provincia, ccaa) -> None:
        self.nombre = nombre
        self.provincia = provincia
        self.ccaa = ccaa

    def funciones(self):
        pass

ciudad1 = Ciudad("Barcelona","Barcelona","Catalunya")
generar_pdf(ciudad1, "capital.pdf")
