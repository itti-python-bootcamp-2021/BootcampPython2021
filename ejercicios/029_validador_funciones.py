def calcular_riesgos(nombre, ciudad=None, edad=18):
    if (ciudad==None):
        raise Exception("No se ha indicado la ciudad")
    riesgo = len(nombre) + edad + len(ciudad)/2
    return riesgo

#Llamada con el tratamiento de las Exceptions
try:
    riesgo = calcular_riesgos("Ricardo")
    print(riesgo)
except Exception as e:
    print("Ha ocurrido un error:", e)