from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    elenco = models.CharField(max_length=20)
    puntaje = models.IntegerField()

class Director(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)
