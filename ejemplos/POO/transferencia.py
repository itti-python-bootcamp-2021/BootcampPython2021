from generador_pdfs import generar_pdf

class Transferencia:
    COMISION = 0.1
    def __init__(self, origen, destino, importe, emisor, destinatario) -> None:
        self.origen = origen
        self.destino = destino
        self.importe = importe
        self.emisor = emisor
        self.destinatario = destinatario

    def __str__(self) -> str:
        salida = self.origen + ":" + self.destino + ":" + str(self.importe) + ":" + self.emisor + ":" + self.destinatario
        return salida

    def calcular_comision(self):
        print("Calculando comisión...")
        comision = self.importe/100*Transferencia.COMISION
        return comision

    def mostrar_datos(self):
        print("**********")
        print(self.origen)
        print(self.destino)
        print(str(self.importe) + "€")
        print(self.emisor)
        print(self.destinatario)
        print("**********")
    
    def generar_pdf(self, nombre_fichero):
        print("Generando pdf...")
        with open(nombre_fichero, "w") as fichero:
            fichero.write(str(self))

transferencia1 = Transferencia("12345","84832",300,"Mohamed","Fernando")
#comision = transferencia1.calcular_comision()
#print(comision)
#transferencia1.mostrar_datos()
#print(transferencia1)
#transferencia1.generar_pdf("salida.pdf")
generar_pdf(transferencia1, "salida.pdf")
