#Pedir una contraseña al usuario
#Comprobar que no contiene ninguna palabra de las contenidas en el fichero 100_Palabras_Castellano.txt
#"100_Palabras_Castellano.txt"
NOMBRE_FICHERO = "Palabras_Castellano.txt"

with open(NOMBRE_FICHERO,"r",encoding="UTF-8") as fichero:
    palabras_prohibidas = fichero.read().splitlines()

password = input("Introduce la contraseña:")

"""
numero_de_veces = password.count(prohibida) #Si es 0 es que no está. Si es >0 es que está contenida.
posicion = password.find(prohibida) #Si es -1 es que no está. Si >=0 es que está contenida.
esta_contenida = prohibida in password #True o False si está contenida o no
"""

esta_permitida = True
for palabra_prohibida in palabras_prohibidas:
    if (len(palabra_prohibida)==1):
        continue
    if (palabra_prohibida in password):
        esta_permitida = False
        print("La contraseña no es correcta")
        break
if (esta_permitida):
    print("La contraseña es correcta")

    
    
