def get_capital(nombre):
    with open("capitales.txt","r",encoding="UTF-8") as capitales:
                paises = capitales.readlines()
                capital=""
                for pais in paises:
                    nombre_pais, nombre_capital = pais.split(":")
                    if (nombre_pais==nombre):
                        capital = nombre_capital[:-1]
                        break
                if (capital==""):
                    raise Exception("No se ha encontrado el país")
    return capital