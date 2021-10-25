#https://www.w3resource.com/python-exercises/string/
#Ejercicio 5
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
cadena1 = "hola"
cadena2 = "adios"
#Resultado esperado: adla hoios
cadena1_final = cadena2[0:2] + cadena1[2:]
cadena2_final = cadena1[0:2] + cadena2[2:]
resultado = cadena1_final + " " + cadena2_final
print(resultado)
#print (cadena2[0:2] + cadena1[2:] + " " + cadena1[0:2] + cadena2[2:])
