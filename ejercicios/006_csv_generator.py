dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes"]
ingresos_online = ("10","20","15","12","88")
ingresos_tienda = ("30","5","10","80","150")
#Generar un fichero CSV y escribir el resultado
fichero = open("salida.csv","w",encoding="utf8")
#fichero.write(",".join(dias_semana))
fichero.write(",".join(dias_semana))
fichero.write("\n")
fichero.write(",".join(ingresos_online))
fichero.write("\n")
fichero.write(",".join(ingresos_tienda))
fichero.close()