#https://www.w3resource.com/python-exercises/string/
#Ejercicio 3
cadena = "FABULOSO"
#cadena = "FA"
#cadena = "F"
resultado = ""
if len(cadena)<2:
    resultado="Empty String"
else:
    primer_bloque = cadena[:2]
    #segundo_bloque = cadena[-2:]
    segundo_bloque = cadena[len(cadena)-2:]
    resultado = primer_bloque+segundo_bloque
print(resultado)