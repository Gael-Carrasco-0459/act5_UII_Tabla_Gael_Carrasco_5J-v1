from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre= models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    edad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.edad}"
    