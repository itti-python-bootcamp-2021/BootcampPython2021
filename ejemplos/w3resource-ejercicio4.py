#https://www.w3resource.com/python-exercises/string/
#Ejercicio 4
palabra = "barrabasada"
primera_letra = palabra[0]
palabra = palabra.replace(primera_letra,"$")
nueva_palabra = primera_letra + palabra[1:] 
print(nueva_palabra)