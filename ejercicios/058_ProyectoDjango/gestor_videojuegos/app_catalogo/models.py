from django.db import models

# Create your models here.

class Videojuego(models.Model):
    #id --> Se genera automaticamente
    titulo=models.CharField(max_length=100)
    plataforma=models.CharField(max_length=100)
    genero=models.CharField(max_length=100)
    precio=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.titulo}-{self.plataforma}-{self.genero}-{self.precio}"


class Plataforma(models.Model):
    #id --> Se genera automaticamente
    nombre=models.CharField(max_length=30)
    fabricante=models.CharField(max_length=20)



