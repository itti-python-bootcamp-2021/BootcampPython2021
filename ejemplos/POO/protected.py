class Banco:
    def __init__(self, nombre, propietario) -> None:
        self.nombre = nombre
        self.__propietario = propietario
        
    @property
    def propietario(self):
        print("get")
        return self.__propietario

    @propietario.setter
    def propietario(self, value):
        print("set")
        self.__propietario = value

b = Banco("Banco de Torrelavega","D. Vicent Price ")
print(b.propietario)
b.propietario="Boris Karloff"
print(b.propietario)