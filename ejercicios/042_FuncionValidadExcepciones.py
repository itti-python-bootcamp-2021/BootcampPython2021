"""
Crear la función:
validar_formulario(nombre : str, email : str, ciudad: str, edad:int) : none
Validar mediante el uso de excepciones:
--- El nombre es correcto. Tiene más 10 caracteres.
--- El email es correcto. Tiene el símbolo de la @
--- Que la ciudad está dentro de una lista de tupla
--- Que la edad es >= 18, y que la edad<65
"""
class CiudadNoValidaError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class EdadNoValidadError(Exception):
    def __init__(self, *args: object, tipo) -> None:
        super().__init__(*args)
        self.tipo = tipo
    
    def notificar(self):
        print("Notificando el problema...")

ciudades = ("Barcelona","Bilbao","Madrid","Sevilla","Valencia")
def validar_formulario(nombre : str, email : str, ciudad: str, edad: int) -> None:
    if (len(nombre)<=10):
        raise ValueError("Longitud del nombre insuficiente")
    if (not "@" in email):
        raise ValueError("El email no contiene @")
    if (ciudad not in ciudades):
        raise CiudadNoValidaError("La ciudad no está en la lista")
    if (edad<18):
        raise EdadNoValidadError("La edad no es válida por ser menor de edad", tipo=0)
    if (edad>=65):
        raise EdadNoValidadError("La edad no es válida por ser mayor de edad", tipo=1)
try:
    validar_formulario("Fernando Paniagua","fernando@gmail.com","Valencia",15)
except CiudadNoValidaError as e:
    #Hacemos más cosas que en el except anterior
    print("Error en la ciudad, no está en la lista")
except ValueError as e:
    print(e)
except EdadNoValidadError as e:
    e.notificar()
    print("Mensaje de la excepcion:", e)
    if (e.tipo == 0):
        print("La edad no es válida: es menor de edad")
    elif (e.tipo == 1):
        print("La edad no es válida: es mayor de edad")