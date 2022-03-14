from django.urls import path
from vj_app.views import VideojuegoView
urlpatterns = [

path('videojuego/', VideojuegoView.as_view(), name="find_all_videojuegos"),

path('videojuego/<str:titulo>/<str:genero>/<str:plataforma>/<int:anyo>/', VideojuegoView.as_view(), name="create_videojuego"),

path('videojuego/<int:id>/<str:titulo>/<str:genero>/<str:plataforma>/<int:anyo>/', VideojuegoView.as_view(),name="update_videojuego"),

path('videojuego/<int:id>/', VideojuegoView.as_view(), name="delete_videojuego"),

]