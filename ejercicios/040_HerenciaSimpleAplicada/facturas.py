class Factura:
    def __init__(self, numero, nombre_cliente, importe) -> None:
        self.numero = numero
        self.nombre_cliente = nombre_cliente
        self.importe = importe

    def generar_documento(self, nombre_fichero):
        with open(nombre_fichero+".txt","w") as fichero:
            fichero.write(str(self.numero))
            fichero.write("\n")
            fichero.write(self.nombre_cliente)
            fichero.write("\n")
            fichero.write(str(self.importe))
            fichero.write("\n")

class FacturaPDF(Factura):
    def generar_documento(self, nombre_fichero):
        #Hago trampa, porque tendría que generar un documento PDF
        with open(nombre_fichero+".pdf","w") as fichero:
            fichero.write(str(self.numero))
            fichero.write("\n")
            fichero.write(self.nombre_cliente)
            fichero.write("\n")
            fichero.write(str(self.importe))
            fichero.write("\n")

Factura(1,"Fernando",1000).generar_documento("factura")
FacturaPDF(2,"Mohamed",2000).generar_documento("factura")