from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_catalogo.models import Videojuego

# Create your views here.

def home(request):
    return render(request, "home.html")

def crear_videojuego(request):
    return render(request, "crear_videojuego.html")

def mostrar_videojuegos(request):
    videojuegos = Videojuego.objects.all()#Acceso a la base de datos
    datos = {"juegos":videojuegos}
    plantilla = loader.get_template("mostrar_videojuegos.html")
    documento = plantilla.render(datos)#'Renderizado' de la plantilla
    return HttpResponse(documento)

def crear_videojuego_bbdd(request):
    _nombre = request.GET["nombre"]
    _plataforma = request.GET["plataforma"]
    _genero = request.GET["genero"]
    v = Videojuego(titulo=_nombre, plataforma=_plataforma, genero=_genero, precio=10)
    v.save()#Acceso a la base de datos
    return mostrar_videojuegos(request)