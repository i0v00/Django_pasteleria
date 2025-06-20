from django.db import models

class Usuario(models.Model):
    ROLES = (('admin', 'Admin'), ('vendedor', 'Vendedor'))
    nombreuser = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    correouser = models.EmailField(max_length=100, blank=True, null=True)
    clave = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=ROLES, default='vendedor')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreuser
