#fichero = open("Presion-Arterial-16-11-2021.csv","r",encoding="UTF-8")
#Aquí va el código de lectura
#fichero.close()

with open("Presion-Arterial-16-11-2021.csv","r",encoding="UTF-8") as fichero:
    lineas = fichero.readlines()[1:] #Leemos todas las líneas y descartamos la primera
    presiones = []
    for linea in lineas:
        datos = linea.split(",")
        datos.pop(6) #Eliminamos el elemento '\n'
        presiones.append(datos)
    #En este punto tenemos la lista de mediciones (listas de fecha, hora, sistolica, diastolica, pulsaciones, calificación textual)
    for presion in presiones:#Convertir los elementos numéricos de str a int (conversión de tipo - cast)
        presion[2]=int(presion[2])
        presion[3]=int(presion[3])
        presion[4]=int(presion[4])
    #presiones es una lista con todas las lecturas en formato [fecha,hora,sistolica,diastolica,pulsaciones,texto]
    """
    1. Mostrar la fecha y la hora de las tensiones más altas (sistólica)
    2. Mostrar la fecha y la hora de las tensiones más bajas (diastólica)
    3. Mostrar la fecha y la hora de las pulsaciones máximas y mínimas.
    4. Media de tensiones sistólicas.
    5. Media de tensiones diastólicas.
    6. Media de pulsaciones.
    """
    maxima_sistolica = presiones[0]
    minima_diastolica = presiones[0]
    maxima_pulsaciones = presiones[0]
    minima_pulsaciones = presiones[0]
    suma_sistolicas = 0
    suma_diastolica = 0
    suma_pulsaciones = 0
    for presion in presiones:
        if presion[2]>maxima_sistolica[2]:
            maxima_sistolica = presion
        if presion[3]<minima_diastolica[3]:
            minima_diastolica = presion
        if presion[4]>maxima_pulsaciones[4]:
            maxima_pulsaciones = presion
        if presion[4]<minima_pulsaciones[4]:
            minima_pulsaciones = presion
        suma_sistolicas+=presion[2]
        suma_diastolica+=presion[3]
        suma_pulsaciones+=presion[4]
    
    print("Max. sis.:", maxima_sistolica[2], maxima_sistolica)
    print("Min. dia.:", minima_diastolica[3], minima_diastolica)
    print("Max. pul.:", maxima_pulsaciones[4], maxima_pulsaciones)
    print("Min. pul.:", minima_pulsaciones[4], minima_pulsaciones)
    numero_lecturas = len(presiones)
    print("Media sistolica:", suma_sistolicas/numero_lecturas)
    print("Media diastolica:", suma_diastolica/numero_lecturas)
    print("Media pulsaciones:", suma_pulsaciones/numero_lecturas)