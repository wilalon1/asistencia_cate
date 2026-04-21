from django.db import models

from apps.asistencia.models import Persona
# Create your models here.
class Ocupacion(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)


class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_nacimiento = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	ocupacion = models.ManyToManyField(Ocupacion, blank=True)