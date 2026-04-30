from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    fechaNacimiento = models.DateField()
    domicilio = models.TextField()
    telefonoPadre = models.CharField(max_length=12)
    telefonoMadre = models.CharField(max_length=12)
    Bautismo = models.BooleanField(default=True)
    Comunion = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

class AsistenciaCabecera(models.Model):
    descripcion = models.CharField(max_length=700)
    acronimo = models.CharField(max_length=700)
    estado = models.BooleanField(default=True)
    
    def __str__(self):  # 👈 opcional pero recomendable
        return self.descripcion


class AsistenciaDetalle(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    asistenciaCabecera = models.ForeignKey(AsistenciaCabecera, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()
    estado = models.BooleanField(default=True)
    observacion = models.CharField(max_length=700, default='-')
    
    def __str__(self):  # 👈 AQUÍ VA
        return f"{self.asistenciaCabecera} | {self.persona} | {self.fecha}"
    

