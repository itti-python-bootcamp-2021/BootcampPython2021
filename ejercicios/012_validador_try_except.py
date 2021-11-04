try:
    dividendo = int(input("Introduce dividendo:"))
    divisor = int(input("Introduce divisor:"))
    resultado = dividendo/divisor
    print("El resultado es",resultado)
except ValueError:
    print("Algunos de los operandos no es un entero")
except ZeroDivisionError:
    print("Error de división entre zero")
except ArithmeticError:
    print("Error aritmético")
except BaseException:
    print("Error de excepcion genérica")
except Exception:
    print("Error de cualquier exception")
except:
    print("Contacte con el administrador porque no sé qué pasa")
