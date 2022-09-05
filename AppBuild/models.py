from django.db import models


class Obra(models.Model):
    tipo = models.CharField(max_length=40)
    inicio = models.CharField(max_length=40)

#    def __str__(self):
#        return f"Curso: {self.nombre}, Camada: {self.camada}"


class Obrero(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()


class Arquitecto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=30)
