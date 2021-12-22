from persistencia.gestor_peliculas import GestorBBDD
from model.pelicula import Pelicula

gestor = GestorBBDD("./datos/base_de_datos_oo.db")
#gestor.crear_esquema_normal()
pelicula = Pelicula("El Resplandor","Kubrick",1978, "Paramount")
gestor.create(pelicula)