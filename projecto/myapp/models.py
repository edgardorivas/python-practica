from django.db import models

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete = models.CASCADE)
