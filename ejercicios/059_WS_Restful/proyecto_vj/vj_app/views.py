from django.shortcuts import render

# Create your views here.

from django.views import View #Para realizar las vistas basadas en clases en lugar de funciones
from vj_app.models import Videojuego #Modelo
from django.http import JsonResponse #Conversor a JSON
from django.core.exceptions import ObjectDoesNotExist #Excepción de objeto no encontrado

from django.utils.decorators import method_decorator #Para desactivar la protección frente a Cross Site Request Forgery (CSRF)
from django.views.decorators.csrf import csrf_exempt #Para desactivar la protección frente a Cross Site Request Forgery (CSRF)

@method_decorator(csrf_exempt, name='dispatch')
class VideojuegoView(View):
    def get(self, request):
        videojuegos = Videojuego.objects.all()
        return JsonResponse(list(videojuegos.values()), safe=False)

    def post(self, request, titulo, genero, plataforma, anyo):
        Videojuego(titulo=titulo, genero=genero,plataforma=plataforma, anyo=anyo).save()
        retorno = {"code":0,"message":"OK"}
        return JsonResponse(retorno)

    def put(self, request, id, titulo, genero, plataforma, anyo):
        try:
            videojuego = Videojuego.objects.get(pk=id)
            videojuego.titulo = titulo
            videojuego.genero = genero
            videojuego.plataforma = plataforma
            videojuego.anyo = anyo
            videojuego.save()
            retorno = {"code":0,"message":"Ok"}
        except ObjectDoesNotExist:
            retorno = {"code":1,"message":"Entidad no existente"}
        except:
            retorno = {"code":2,"message":"Error desconocido"}
        return JsonResponse(retorno)

    def delete(self, request, id):
        try:
            Videojuego.objects.get(pk=id).delete()
            retorno = {"code":0,"message":"Ok"}
        except:
            retorno = {"code":-1,"message":"Ha ocurrido un error"}
        return JsonResponse(retorno)