telefonos = []
with open("telefonos_moviles.datos","r",encoding="utf-8") as fichero:
    while True:
        modelo = fichero.readline()[:-1]
        if (modelo==""):
            break
        fabricante = fichero.readline()[:-1]
        precio = fichero.readline()[:-1]
        telefonos.append([modelo,fabricante,precio])
print(telefonos)