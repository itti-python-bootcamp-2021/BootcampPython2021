from django.http import HttpResponse
from django.template import loader

def saludador(request):
    return HttpResponse("Hola a todos")

def saludador_personalizado(request, nombre, edad):
    return HttpResponse("Hola " + nombre + " " + str(edad))

def mostrar_plantilla(request):
    #Obtener los datos
    importe = 15000
    #Generar los parámetros para la plantilla
    datos = {"importe":importe}
    #Obtener la plantilla
    plantilla = loader.get_template("miplantilla.html")
    #Generar la vista
    documento = plantilla.render(datos)#'Renderizado' de la plantilla
    return HttpResponse(documento)

