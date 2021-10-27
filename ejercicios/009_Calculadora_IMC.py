"""
Pedir al usuario su altura y su peso e indicarle en que posición de la tabla está 
IMC = dividiendo los kilogramos de peso por el cuadrado de la estatura en metros 
Delgadez < 18.5
Normal	18.5 – 24.9
Sobrepeso	25.0 – 29.9
Obesidad	Igual o más de 30.0
"""
def calcular_IMC(peso, altura):
    #imc = peso / (altura * altura)
    imc = peso / altura ** 2
    imc = round(imc, 2) #Redondear a dos decimales
    return imc

def calcular_estado(imc):
    estado=""
    if imc<18.5:
        estado = "Delgadez"
    elif imc>=18.5 and imc<25.0:
        estado = "Normal" 
    elif imc>=25.0 and imc<30.0:
        estado = "Sobrepeso"
    elif imc>=30:
        estado = "Obesidad"
    return estado

altura = float(input("Introduce tu altura en metros:"))
peso = float(input("Introduce tu peso en kilogramos:"))
imc = calcular_IMC(peso, altura)
estado = calcular_estado(imc)

print("El IMC del paciente es:", imc)
print("El estado del paciente es",estado)

