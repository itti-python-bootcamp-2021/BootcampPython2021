dividendo = 100
divisor = 0
try:
    print(dividendo.isdigit())
    resultado = dividendo / divisor
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except AttributeError:
    print("Error en la llamada a isdigit")
except:
    print("No sé qué ha ocurrido pero lo gestiono")