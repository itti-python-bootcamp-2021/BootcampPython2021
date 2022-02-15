import re
cadena = """
Mi dirección de correo electrónico es
fernando.paniagua.formacion@gmail.com. conejo
Hay otras direcciones de correo electronico, pero son privadas.
ME GUSTA EL CORREO ELECTRÓNICO
tengo correo hhhelectronico
¿Existe la palabra electrínico?
"""
#EJEMPLO SENCILLO DE SEARCH
texto_a_buscar = "correo"
texto_encontrado = re.search(texto_a_buscar, cadena)
if texto_encontrado is not None:
    print(texto_encontrado.span())
    print(texto_encontrado.start())
    print(texto_encontrado.end())
else:
    print("Texto no encontrado")
#EJEMPLO SENCILLO DE FINDALL
texto_encontrado = re.findall(texto_a_buscar, cadena)
print(texto_encontrado) #Muestra una lista
texto_encontrado = re.findall("c[a-zA-Z]+o",cadena)#Todas las cadenas que empiezan por c, tienen uno más letras, y terminan por o
print(texto_encontrado) #Muestra una lista

print(re.findall("^Mi",cadena))#Empieza por
print(re.findall("privadas$",cadena))#Termina por
print(re.findall("[abc]",cadena))#Contiene las letras a, b ó c
print(re.findall("[@:]gmail", cadena))#Contiene @ o : y después gmail
print(re.findall("[a-d]",cadena))#Contiene las letras entre la a y la d minúsculas
print(re.findall("[a-zA-Z]", cadena))#Todas las letras mayúsculas y minúsculas
print(re.search("[@#]",cadena))#Si contiene el carácter @ o #

print(re.findall("electr[oó]nico", cadena, re.IGNORECASE))#electrónico o electronico
print(re.findall("[h]?electr[oó]nico", cadena, re.IGNORECASE)) #electrónico o electronico o helectronico o helectrónico o HELECTRONICO...

print(re.findall("electr[^oó]nico", cadena, re.IGNORECASE))#Exclusión de las letras o y ó

def validar(direccion):
    expresion = "[a-z]+(\.[a-z]+)*@[a-z]+\.(com|es)"
    return re.match(expresion,direccion)

direcciones = []
direcciones.append("fernando.paniagua.formacion@gmail.com")
direcciones.append("fernando.paniagua.formacion@gmail")
direcciones.append("fernando.paniagua.formacion@hotmail.es")
direcciones.append("fernando.paniagua.formacion@hotmail.it")
direcciones.append("@hotmail.it")
direcciones.append("fernando.paniagua@gmail.com")
direcciones.append("fernando@gmail.com")
validaciones = list(map(validar, direcciones))
for validacion in validaciones:
    print(validacion)


