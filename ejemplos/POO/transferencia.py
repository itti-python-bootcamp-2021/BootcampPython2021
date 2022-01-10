class Transferencia:
    COMISION = 0.1
    def __init__(self, origen, destino, importe, emisor, destinatario) -> None:
        self.origen = origen
        self.destino = destino
        self.importe = importe
        self.emisor = emisor
        self.destinatario = destinatario

    def calcular_comision(self):
        print("Calculando comisión...")

    def mostrar_datos(self):
        print("**********")
        print(self.origen)
        print(self.destino)
        print(str(self.importe) + "€")
        print(self.emisor)
        print(self.destinatario)
        print("**********")
        
    def generar_pdf(self):
        print("Generando pdf...")

transferencia1 = Transferencia("12345","84832",300,"Mohamed","Fernando")
transferencia1.calcular_comision()
transferencia1.mostrar_datos()
transferencia1.generar_pdf()


