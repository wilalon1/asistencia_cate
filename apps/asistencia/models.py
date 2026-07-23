from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey



class AsistenciaCabecera(models.Model):
    descripcion = models.CharField(max_length=700)
    acronimo = models.CharField(max_length=700)
    estado = models.BooleanField(default=True)
    
    def __str__(self):  # 👈 opcional pero recomendable
        return self.descripcion
    
# Create your models here.
class Persona(models.Model):
    asistenciaCabecera = models.ForeignKey(
        AsistenciaCabecera,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    domicilio = models.TextField()
    telefonoPadre = models.CharField(max_length=12)
    telefonoMadre = models.CharField(max_length=12)
    Bautismo = models.BooleanField(default=True)
    Comunion = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos, self.codigo)


class UsuarioAsistencia(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    asistenciaCabecera = models.ForeignKey(
        AsistenciaCabecera,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.usuario.username



class AsistenciaDetalle(models.Model):

    #persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    asistenciaCabecera = models.ForeignKey(AsistenciaCabecera, on_delete=models.SET_NULL, null=True, blank=True)
    persona = ChainedForeignKey(
        Persona,
        chained_field="asistenciaCabecera",
        chained_model_field="asistenciaCabecera",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    fecha = models.DateField()
    estado = models.BooleanField(default=True)
    observacion = models.CharField(max_length=700, default='-')

    catequesis = models.BooleanField(default=True)
    misa = models.BooleanField(default=True)
    justificado = models.BooleanField(default=False)
    ##corpus = models.BooleanField(default=True)

    def __str__(self):
        tipos = []
        if self.catequesis:
            tipos.append("C")
        if self.misa:
            tipos.append("M")
        if self.justificado:
            tipos.append("JJ")

        return f"{self.asistenciaCabecera} | {self.persona} | {self.fecha} | {' '.join(tipos)}| {self.observacion}" 
