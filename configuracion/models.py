from django.db import models

class Configuracion(models.Model):
    nit = models.CharField(max_length=20)
    nombreconfig = models.CharField(max_length=100)
    telefonoconfig = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    razonsocial = models.CharField(max_length=100, blank=True, null=True)
