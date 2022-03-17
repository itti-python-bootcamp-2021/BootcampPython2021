from django.http import HttpResponse
from django.template import loader

def cliente_ws_js(request):
    plantilla = loader.get_template("cliente.html")
    return HttpResponse(plantilla.render())