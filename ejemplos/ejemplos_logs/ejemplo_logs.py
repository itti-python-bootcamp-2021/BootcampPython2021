import logging

def inicializar():
    #logging.getLogger().setLevel(logging.ERROR) #Asignación de nivel
    logging.basicConfig(
        filename="I:/logs/fichero_salida.log",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.ERROR)


def funcion1():
    print("Función 1...")
    logging.debug("Ejecutando función 1")

def funcion2():
    print("Función 2...")
    edad=105
    if (edad>100):
        logging.info("Se ha registrado un usuario con más de 100 años")

def funcion3():
    print("Función 3...")
    try:
        if (8/0)==10:
            a = 8
    except ZeroDivisionError as zde:
        #logging.error("El divisor de la operación es 0") #No muestra la información proporcionada por la excepción
        logging.exception(zde) #Muestra la información proporcionada por la excepción

if __name__ == '__main__':
    inicializar()
    funcion1()
    funcion2()
    funcion3()