fichero = open("elquijote.txt","r", encoding="utf8")
texto = fichero.read()
fichero.close()
#1. Solicitar una palabra al usuario
palabra = input("Introduce una palabra:")
#2. Vamos a indicar si existe la palabra en el texto y cuantes veces aparece
# (sin tener en cuenta si está en mayúsculas o minúsculas) lower, upper, count, index, find
palabra_mayuscula = palabra.upper()
texto_mayuscula = texto.upper()
if palabra_mayuscula in texto_mayuscula:
    print("La palabra existe")
    print("Número de veces",texto_mayuscula.count(palabra_mayuscula))
else:
    print("La palabra no existe")    
#3. Solicitar un nombre al usuario
nombre = input("Dime tu nombre:")
#4. Vamos a reemplazar a Sancho por ese nombre utilizando replace(old, new[, count])
texto_modificado = texto.replace("Sancho",nombre)
#5. Escribir la nueva versión
fichero = open("elquijote_modificado.txt","w",encoding="utf8")
fichero.write(texto_modificado)
fichero.close()