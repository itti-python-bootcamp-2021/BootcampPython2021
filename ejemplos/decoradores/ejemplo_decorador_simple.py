def funcion_principal(funcion):
    print("Inicio principal...")
    def envoltorio():
        print("Inicio wrapper...")#Opcional
        funcion()#Opcional
        print("Fin wrapper...")#Opcional
    print("Fin principal...")
    return envoltorio

@funcion_principal
def saludar():
    print("Hola")

saludar()