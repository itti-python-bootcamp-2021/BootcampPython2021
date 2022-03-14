from django.db import models

# Create your models here.

class Videojuego(models.Model):
    #id (se genera automáticamente)
    titulo=models.CharField(max_length=100,null=False)
    genero=models.CharField(max_length=100,null=False)
    plataforma=models.CharField(max_length=50,null=False)
    anyo=models.IntegerField(null=False)