def funcion1():
    print("No tengo información")

def funcion2(parametro):
    print(parametro)

def funcion3(parametro1, parametro2):
    print(parametro1,parametro2)

def funcion4(parametro1, parametro2, parametro3="Por defecto"):
    print(parametro1, parametro2, parametro3)

def funcion5(parametro3, parametro1="Por defecto", parametro2="Por defecto"):
    print(parametro3,parametro1,parametro2)

def funcion6(parametro1, *parametros2):
    print(parametro1)
    for parametro in parametros2:
        print(parametro)

def funcion7(parametro1, parametro2, parametro3):
    print(parametro1, parametro2, parametro3)

funcion1()
funcion2("Google")
funcion3("Google","Amazon")
funcion4("BMW","Seat")
funcion4("BMW","Seat","Renault")
funcion5("Colacao")
funcion5("Colacao","Cacaolat")
funcion5("Colacao","Cacaolat","Nesquick")
funcion6("Lauki")
funcion6("Lauki","Pascual")
funcion6("Lauki","Pascual","PMI")
funcion6("Lauki","Pascual","PMI","RAM")
funcion7(parametro2="Call Of Duty", parametro3="Battlefield 3", parametro1="Grand Theft Auto V")
funcion7(None,None,None)