from typing import Any
from django.db import models

class Estudiante(models.Model):
    identificacion = models.IntegerField(null=False)
    nombre = models.CharField(max_length=30, null=False)
    apellido_1 = models.CharField(max_length=15, null=False)
    apellido_2 = models.CharField(max_length=15, null=False)
    

# Create your models here.
