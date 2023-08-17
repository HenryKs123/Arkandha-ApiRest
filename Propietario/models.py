from django.db import models

# Create your models here.
class Propietario(models.Model):
    
    NombreP = models.CharField(max_length=30)
    NombreS = models.CharField(max_length=30)
    ApellidoP = models.CharField(max_length=30)
    ApellidoS = models.CharField(max_length=30)
    Documento = models.CharField(max_length=30)
    NumeroDocumento = models.IntegerField()
