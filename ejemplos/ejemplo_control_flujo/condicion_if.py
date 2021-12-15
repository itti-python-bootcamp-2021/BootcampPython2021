edad = 19
sexo = "Mujer"
altura = 170
peso = 72
nacionalidad = "Noruego"
color_ojos = "Azul"

#mayor de edad, mujer, mas de 175, peso menos de 80, nacionalidad = noruega, color_ojos = "verde"
#if (edad>=18 and sexo=="Mujer" and altura>180 and peso<80 and nacionalidad="Noruega" and color_ojos="Verde")

fisico = altura>180 and peso<80
origen = edad>=18 and nacionalidad=="Noruega"
genetico= sexo=="Mujer" and color_ojos=="Verde"

if (fisico and origen and genetico):
    #candidato
    pass