from django.db import models

# Create your models here.

class Argentino(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()

class Extranjero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40) 

class Nacionalizado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()