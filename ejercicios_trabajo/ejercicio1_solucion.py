def generar_html(nombre, numero_telefono, direccion_correo, fecha_nacimiento, idioma, calle, poblacion, cp):
    #Generar fichero HTML.
    nombre_fichero = nombre + ".html"
    pagina = open(nombre_fichero,"w",encoding="utf-8")
    pagina.write("<!DOCTYPE html>")
    pagina.write("<html lang=\""+idioma+"\">")
    pagina.write("\n")
    pagina.write("<head><meta charset=\"UTF-8\"><title>FORMULARIO</title></head>")
    pagina.write("\n")
    pagina.write("<body>")
    pagina.write("\n")
    pagina.write("<h3>Nombre: "+nombre+"</h3>")
    pagina.write("\n")
    pagina.write("<p>Numero telefono: "+numero_telefono+"</p>")
    pagina.write("\n")
    pagina.write("<p>Correo: "+direccion_correo+"</p>")
    pagina.write("\n")
    pagina.write("<p> Fecha nacimiento: "+fecha_nacimiento+"</p>")
    pagina.write("\n")
    pagina.write("<h3>Domicilio</h3>")
    pagina.write("\n")
    pagina.write("<p>Calle: "+calle+"</p>")
    pagina.write("\n")
    pagina.write("<p>Poblacion: "+poblacion+"</p>")
    pagina.write("\n")
    pagina.write("<p>Codigo postal: "+cp+"</p>")
    pagina.write("\n")
    pagina.write("</body>")
    pagina.write("\n")
    pagina.write("</html>")
    pagina.close()

idiomas_validos = ["ES","EN","FR"]
while True:
    numero_errores = 0
    #INTRODUCCIÓN DE DATOS
    print("***** DATOS PERSONALES *****")
    nombre = input("Introduce tu nombre:")
    numero_telefono = input("Introduce tu número de teléfono:")
    direccion_correo = input("Introduce tu dirección de correo electrónico:")
    fecha_nacimiento = input("Introduce la fecha de nacimiento (dd/mm/aaaa):")
    idioma = input("Idioma (ES/EN/FR):")
    print("***** DIRECCIÓN *****")
    calle = input("Calle:")
    poblacion = input("Población:")
    cp = input("Código Postal:")
    
    #VALIDACIONES
    nombre_valido = len(nombre) >= 5 and ("ñ" not in nombre.lower())
    numero_telefono_valido = numero_telefono.isdigit()
    email_valido = (len(direccion_correo)>=10) and ("@" in direccion_correo) and ("." in direccion_correo)
    fecha_nacimiento_valida = fecha_nacimiento[:2].isdigit() and fecha_nacimiento[2]=="/" and fecha_nacimiento[3:5].isdigit() and fecha_nacimiento[5] =="/" and fecha_nacimiento[6:].isdigit()
    calle_valida = len(calle)>=10
    poblacion_valida = len(poblacion)>=5
    cp_valido = len(cp)==5 and cp.isdigit()
    #idioma_valido = idioma=="ES" or idioma=="EN" or idioma=="FR"
    idioma_valido = idioma in idiomas_validos

    #REPASAR Y MOSTRAR LOS MENSAJES DE ERROR SI APLICA      
    if not nombre_valido:
        numero_errores+=1
        print("El nombre es incorrecto")
    if not numero_telefono_valido:
        numero_errores+=1
        print("El número es incorrecto")
    if not email_valido:
        numero_errores+=1
        print("El Email no es válido")
    if not fecha_nacimiento_valida:
        numero_errores+=1
        print("La fecha de nacimiento no es válida")
    if not idioma_valido:
        numero_errores+=1
        print("El idioma no es correcto")
    if not calle_valida or not poblacion_valida or not cp_valido:
        numero_errores+=1
        print("Algo en la dirección está mal")
    if numero_errores==0:
        break
generar_html(nombre, numero_telefono, direccion_correo, fecha_nacimiento, idioma, calle, poblacion, cp)