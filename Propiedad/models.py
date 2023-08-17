from django.db import models

# Create your models here.
class Propiedad(models.Model):
    
    Direccion = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=30)
    NCatastral = models.CharField(max_length=30)
    NMatricula = models.CharField(max_length=30)
    IDpropietario = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Dimencion = models.IntegerField()