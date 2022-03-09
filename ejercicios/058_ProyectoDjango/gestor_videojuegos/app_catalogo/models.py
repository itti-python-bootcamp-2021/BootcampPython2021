from django.db import models

# Create your models here.

class Videojuego(models.Model):
    #id
    titulo=models.CharField(max_length=100)
    plataforma=models.CharField(max_length=100)
    genero=models.CharField(max_length=100)
    precio=models.IntegerField()