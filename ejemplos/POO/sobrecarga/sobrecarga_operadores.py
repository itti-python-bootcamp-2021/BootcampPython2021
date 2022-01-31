class Lenguaje:
    def __init__(self, nombre_idioma, pais_origen):
        self.nombre_idioma = nombre_idioma
        self.pais_origen = pais_origen

    def __eq__(self, other):
        return self.nombre_idioma == other.nombre_idioma and self.pais_origen == other.pais_origen

portugues = Lenguaje("portugues","portugal")
brasileiro = Lenguaje("portugues","brasil")
portugais = Lenguaje("portugues","portugal")
otracosa = portugues
print(3==3)
print(portugues==portugais)