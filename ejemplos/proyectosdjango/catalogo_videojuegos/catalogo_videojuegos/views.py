from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse("HOME PAGE")

def saludador(request):
    return HttpResponse("Hola a todos")

def saludador_personalizado(request, nombre, edad):
    return HttpResponse("Hola " + nombre + " " + str(edad))

def mostrar_plantilla(request):
    #Obtener los datos
    importe = 15000
    videojuegos = []
    videojuegos.append([1, "Call of Duty", "FPS"])
    videojuegos.append([2, "Super Mario Kart 8", "Carreras"])
    videojuegos.append([3, "Fifa 2022", "Fútbol"])
    videojuegos.append([4, "Arkanoid", "Arcade"])
    activo = False
    #Generar los parámetros para la plantilla
    datos = {"activo":activo}
    #Obtener la plantilla
    plantilla = loader.get_template("miplantilla.html")
    #Generar la vista
    documento = plantilla.render(datos)#'Renderizado' de la plantilla
    return HttpResponse(documento)