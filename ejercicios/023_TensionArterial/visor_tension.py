import matplotlib.pyplot as plt

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
    presiones.reverse()#Le damos la vuelta para que la primera lectura sea la más antigua en el tiempo

    xs = [i for i in range(1,len(presiones)+1)] #No es obligatorio
    
    ys_sistolicas = []
    for presion in presiones:
        ys_sistolicas.append(presion[2])
        
    ys_diastolicas = [lectura[3] for lectura in presiones]

    pulsaciones = [lectura[4] for lectura in presiones]

    """
    plt.title("Informe médico")
    plt.plot(xs,ys_sistolicas,"green")
    plt.plot(xs,ys_diastolicas,"red")
    plt.plot(pulsaciones,"blue")
    plt.show()
    """

    fig, ax = plt.subplots(3)
    plt.subplots_adjust(hspace=0.6)
    #matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    ax[0].set_title("Sistólica")
    ax[0].plot(xs,ys_sistolicas,"green")
    ax[1].set_title("Diastólica")
    ax[1].plot(xs,ys_diastolicas,"red")
    ax[2].set_title("Pulsaciones")
    ax[2].plot(pulsaciones,"blue")
    
    """
    fig, ax = plt.subplots(2,2)
    ax[0,0].set_title("Sistólica")
    ax[0,0].plot(xs,ys_sistolicas,"green")
    ax[0,1].set_title("Diastólica")
    ax[0,1].plot(xs,ys_diastolicas,"red")
    ax[1,0].set_title("Pulsaciones")
    ax[1,0].plot(pulsaciones,"blue")
    """

    plt.show()

