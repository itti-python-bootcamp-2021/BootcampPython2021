from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def crear_videojuego(request):
    return render(request, "crear_videojuego.html")

def mostrar_videojuegos(request):
    return render(request, "mostrar_videojuegos.html")
