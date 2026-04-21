from django.contrib import admin
from apps.asistencia.models import Persona
from apps.asistencia.models import AsistenciaCabecera
from apps.asistencia.models import AsistenciaDetalle
# Register your models here.
admin.site.register(Persona)
admin.site.register(AsistenciaCabecera)
admin.site.register(AsistenciaDetalle)