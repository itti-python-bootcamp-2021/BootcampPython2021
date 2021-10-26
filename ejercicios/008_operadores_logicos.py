"""
Solicitar la usuario:
- Nombre.
- Año de nacimiento
- Ciudad de residencia.
Hay que indicar si se le va a contratar.
--> Si el nombre tiene más de 8 caracteres, si tiene entre 40 y 40 años, reside en Sevilla o Granada.
"""
nombre_candidato = input("Introduce tu nombre:")
anyo_nacimiento = int(input("Introduce el año de nacimiento:"))
ciudad_residencia = input("Introduce la ciudad de residencia:")

longitud_nombre_valida = len(nombre_candidato) >= 8
edad = 2021-anyo_nacimiento
edad_valida = edad >= 30 and edad <= 40
ciudad_validad = ciudad_residencia=="Sevilla" or ciudad_residencia=="Granada" 

if (longitud_nombre_valida and edad_valida and ciudad_validad):
    print("Eres candidato")
else:
    print("Descartado")
