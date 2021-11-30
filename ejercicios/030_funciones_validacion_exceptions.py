def validar_formulario(nombre, direccion, cp, numero_telefono, email):
    LONGITUD_MINIMA_DIRECCION = 21
    LONGITUD_CP = 5
    #1.Nombre es obligatorio y no puede ser vacio
    nombre = nombre.strip()
    if (len(nombre)==0):
        raise Exception("El nombre no puede estar vacio")
    #2.La dirección tiene que tener más de 20 caracteres
    direccion = direccion.strip()
    if (len(direccion)<LONGITUD_MINIMA_DIRECCION):
        raise Exception ("La dirección debe tener más de 20 caracteres")
    #3.El código postal tiene que ser numérico y de 5 dígitos
    cp = cp.strip()
    if (cp.isdigit()==False):
        raise Exception("El código postal tiene que ser numérico")
    if (len(cp)!=LONGITUD_CP):
        raise Exception("El código postal debe tener 5 dígitos")
    #4.El email tiene que contener una @
    email = email.strip()
    if ("@" not in email):
        raise Exception("La dirección de correo electrónico debe tener una @")

try:
    validar_formulario("Fernando","Avenida de las Retamas 8, Alcorcón","28922","630112233","fernandopaniagua@itti.es")
    print("OK")
except Exception as e:
    print(e)
