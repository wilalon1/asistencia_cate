from django.contrib import admin
from apps.asistencia.models import Persona
from apps.asistencia.models import AsistenciaCabecera
from apps.asistencia.models import AsistenciaDetalle
from apps.asistencia.models import UsuarioAsistencia

#admin.site.register(Persona)
#admin.site.register(AsistenciaCabecera)
#admin.site.register(AsistenciaDetalle)

#from .models import (
#    Persona,
#    AsistenciaCabecera,
#    AsistenciaDetalle,
#    UsuarioAsistencia
#)

admin.site.register(AsistenciaCabecera)
admin.site.register(UsuarioAsistencia)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        try:
            relacion = UsuarioAsistencia.objects.get(
                usuario=request.user
            )

            return qs.filter(
                asistenciaCabecera=relacion.asistenciaCabecera
            )

        except UsuarioAsistencia.DoesNotExist:
            return qs.none()


@admin.register(AsistenciaDetalle)
class AsistenciaDetalleAdmin(admin.ModelAdmin):

    readonly_fields = ('cabecera_usuario',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        try:
            relacion = UsuarioAsistencia.objects.get(
                usuario=request.user
            )

            if db_field.name == 'asistenciaCabecera':
                kwargs['queryset'] = AsistenciaCabecera.objects.filter(
                    pk=relacion.asistenciaCabecera.pk
                )

            if db_field.name == 'persona':
                kwargs['queryset'] = Persona.objects.filter(
                    asistenciaCabecera=relacion.asistenciaCabecera
                )

        except UsuarioAsistencia.DoesNotExist:
            pass

        return super().formfield_for_foreignkey(
            db_field,
            request,
            **kwargs
        )

    def save_model(self, request, obj, form, change):

        if not request.user.is_superuser:

            relacion = UsuarioAsistencia.objects.get(
                usuario=request.user
            )

            obj.asistenciaCabecera = relacion.asistenciaCabecera

        super().save_model(
            request,
            obj,
            form,
            change
        )

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        try:
            relacion = UsuarioAsistencia.objects.get(
                usuario=request.user
            )

            return qs.filter(
                asistenciaCabecera=relacion.asistenciaCabecera
            )

        except UsuarioAsistencia.DoesNotExist:
            return qs.none()
        
        
    #def get_exclude(self, request, obj=None):
    #    if not request.user.is_superuser:
    #        return ('asistenciaCabecera',)
    #    return ()
    
    def cabecera_usuario(self, obj):
        if obj and obj.asistenciaCabecera:
            return obj.asistenciaCabecera.descripcion
        return "-"
    cabecera_usuario.short_description = "Grupo"
    
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if not request.user.is_superuser:
            try:
                relacion = UsuarioAsistencia.objects.get(
                    usuario=request.user
                    )
                extra_context['grupo_usuario'] = (
                    relacion.asistenciaCabecera.descripcion
                    )
            except UsuarioAsistencia.DoesNotExist:
                pass
            
        return super().add_view(
            request,
            form_url,
            extra_context=extra_context
        )