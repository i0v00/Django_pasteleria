from django.db import models

class Producto(models.Model):
    codigoproduct = models.CharField(max_length=30, unique=True)
    nombreproduct = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreproduct
