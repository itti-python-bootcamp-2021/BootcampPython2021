"""gestor_videojuegos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_catalogo.views import home, agregar_producto
from app_catalogo.views import crear_videojuego,  crear_videojuego_bbdd, mostrar_videojuegos, borrar_videojuego
from app_catalogo.views import crear_plataforma, crear_plataforma_bbdd, mostrar_plataformas, borrar_plataforma

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('mostrar_videojuegos/', mostrar_videojuegos),
    path('mostrar_plataformas/', mostrar_plataformas),
    path('crear_videojuego/', crear_videojuego),
    path('crear_plataforma/', crear_plataforma),
    path('crear_videojuego_bbdd/', crear_videojuego_bbdd),
    path('crear_plataformas_bbdd/', crear_plataforma_bbdd),
    path('borrar_videojuego/', borrar_videojuego),
    path('borrar_plataforma/', borrar_plataforma),
    path('agregar_producto/', agregar_producto),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
