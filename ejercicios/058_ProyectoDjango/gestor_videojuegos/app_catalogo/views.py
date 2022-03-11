from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_catalogo.models import Videojuego, Plataforma

# Create your views here.

def home(request):
    return render(request, "home.html")

def mostrar_videojuegos(request):
    videojuegos = Videojuego.objects.all()#Acceso a la base de datos

    importe = 0
    if ('carrito' in request.session):
        for item in request.session["carrito"]:
            importe = importe + int(item[1])

    datos = {"juegos":videojuegos, "importe":importe}
    plantilla = loader.get_template("mostrar_videojuegos.html")
    documento = plantilla.render(datos)#'Renderizado' de la plantilla
    return HttpResponse(documento)

def crear_videojuego(request):
    return render(request, "crear_videojuego.html")

def crear_videojuego_bbdd(request):
    _nombre = request.GET["nombre"]
    _plataforma = request.GET["plataforma"]
    _genero = request.GET["genero"]
    v = Videojuego(titulo=_nombre, plataforma=_plataforma, genero=_genero, precio=10)
    v.save()#Acceso a la base de datos
    return mostrar_videojuegos(request)

def borrar_videojuego(request):
    id = request.GET["id"]
    videojuego = Videojuego.objects.get(id=id)#Leer el videojuego
    videojuego.delete()#Borrado del videojuego
    return mostrar_videojuegos(request)

def mostrar_plataformas(request):
    plataformas = Plataforma.objects.all()

    importe = 0
    if ('carrito' in request.session):
        for item in request.session["carrito"]:
            importe = importe + int(item[1])

    datos = {"plataformas":plataformas, "importe":importe}
    plantilla = loader.get_template("mostrar_plataformas.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def crear_plataforma(request):
    return render(request, "crear_plataforma.html")

def crear_plataforma_bbdd(request):
    nombre = request.GET["nombre"]
    fabricante = request.GET["fabricante"]
    Plataforma(nombre=nombre, fabricante=fabricante).save()
    return mostrar_plataformas(request)

def borrar_plataforma(request):
    id = request.GET["id"]
    plataforma = Plataforma.objects.get(id=id)
    plataforma.delete()
    return mostrar_plataformas(request)

def agregar_producto(request):
    id = request.GET["id"]
    precio = request.GET["precio"]
    if ('carrito' not in request.session):
        request.session['carrito']=[]
    carrito = request.session['carrito']
    carrito.append((id,precio))
    request.session['carrito']=carrito
    return mostrar_videojuegos(request)

