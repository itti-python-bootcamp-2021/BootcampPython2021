#NameError
#ZeroDivisionError
#ValueError
def funcion1():
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
        print(a)
    except:
        print("Ha ocurrido un error.")

def funcion2():
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
        print(a)
    except ZeroDivisionError:
        print("Ha ocurrido un error. El divisor es 0.")
    except ValueError:
        print("Ha ocurrido un error. El divisor no es un número entero")
    except:
        print("Ha ocurrido un error inesperado")

def funcion3():
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
        print(a)
    except  (ZeroDivisionError, ValueError):
        print("Ha ocurrido un error. El divisor es 0 o el número entero.")

def funcion4():
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
        print(a)
    except ZeroDivisionError as zd:
        print(zd)
    except ValueError as ve:
        print(ve)

def funcion5():
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
    except ZeroDivisionError as zd:
        print(zd)
    except ValueError as ve:
        print(ve)
    else:
        print(a)

def funcion5():
    print("INICIO DEL PROCESO")
    try:
        b = int(input("Introduce un número entero:"))
        a = 5/b
        print(a)
    except ZeroDivisionError as zd:
        print(zd)
    except ValueError as ve:
        print(ve)
    finally:
        print("FIN DEL PROCESO")
        


funcion5()