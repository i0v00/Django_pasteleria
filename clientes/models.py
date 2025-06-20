from django.db import models

class Cliente(models.Model):
    cicli = models.CharField(max_length=20)
    nombrecli = models.CharField(max_length=100)
    direccioncli = models.CharField(max_length=150, blank=True, null=True)
    telefonocli = models.CharField(max_length=20, blank=True, null=True)
    estadocli = models.BooleanField(default=True)

    def __str__(self):
        return self.nombrecli
