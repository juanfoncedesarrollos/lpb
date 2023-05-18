from typing import Any
from django.db import models
from cursos.models import Curso

class Estudiante(models.Model):
    identificacion = models.IntegerField(null=False)
    nombre = models.CharField(max_length=30, null=False, unique=True)
    apellido_1 = models.CharField(max_length=15, null=False)
    apellido_2 = models.CharField(max_length=15, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

# Create your models here.
