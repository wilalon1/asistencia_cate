from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.generics import ListAPIView
from datetime import datetime  # 👈 IMPORTANTE

from apps import usuario
from apps.asistencia.models import Persona, AsistenciaCabecera, AsistenciaDetalle,UsuarioAsistencia

#Filtros de pruebas
#http://127.0.0.1:8000/api/asistencia-detalle/?fecha_inicio=01-04-2026&fecha_fin=01-04-2026
#http://127.0.0.1:8000/api/asistencia-detalle/?cabecera_id=1&fecha_inicio=01-04-2026&fecha_fin=30-04-2026
#http://127.0.0.1:8000/api/asistencia-detalle/?cabecera_id=1
#http://localhost:8000/api/asistencia-detalle/?usuario=admin&fecha_inicio=01-06-2026&fecha_fin=30-06-2026
#http://localhost:8000/api/asistencia-usuario/?usuario=admin&fecha_inicio=01-06-2026&fecha_fin=30-06-2026


from .serializers import (
    PersonaSerializer,
    AsistenciaCabeceraSerializer,
    AsistenciaDetalleSerializer,
    AsistenciaUsuarioSerializer
)


def listar(request):

    usuario_asistencia = UsuarioAsistencia.objects.filter(
        usuario=request.user
    ).first()


    return render(
        request,
        'asistencia/listar.html',
        {
            'usuario_asistencia': usuario_asistencia
        }
    )

class PersonaListView(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
    
class PersonaPorUsuarioListView(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):

        usuario = self.request.query_params.get('usuario')

        if not usuario:
            return Persona.objects.none()

        try:
            usuario_asistencia = UsuarioAsistencia.objects.get(
                usuario__username=usuario
            )

            return Persona.objects.filter(
                asistenciaCabecera=usuario_asistencia.asistenciaCabecera
            )

        except UsuarioAsistencia.DoesNotExist:
            return Persona.objects.none()


class AsistenciaCabeceraListView(ListAPIView):
    queryset = AsistenciaCabecera.objects.all()
    serializer_class = AsistenciaCabeceraSerializer


class AsistenciaDetalleListView(ListAPIView):
    serializer_class = AsistenciaDetalleSerializer

    def get_queryset(self):
        queryset = AsistenciaDetalle.objects.all()

        # 🔹 parámetros
        cabecera_id = self.request.query_params.get('cabecera_id')
        usuario = self.request.query_params.get('usuario')
        persona_id = self.request.query_params.get('idPersona')
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')
        observacion = self.request.query_params.get('observacion')  # 👈 NUEVO
        
        if usuario:

            try:

                usuario_asistencia = UsuarioAsistencia.objects.get(
                    usuario__username=usuario
                )


                queryset = queryset.filter(
                    asistenciaCabecera=
                    usuario_asistencia.asistenciaCabecera
                )


            except UsuarioAsistencia.DoesNotExist:

                return AsistenciaDetalle.objects.none()

        # 🔹 filtro por cabecera
        if cabecera_id:
            queryset = queryset.filter(asistenciaCabecera_id=cabecera_id)

        # 🔹 filtro por persona
        if persona_id:
            queryset = queryset.filter(persona_id=persona_id)

        # 🔹 filtro por observación (J o A)
        if observacion:
            queryset = queryset.filter(observacion__iexact=observacion)


        # 🔹 filtro por fechas
        try:
            if fecha_inicio and fecha_fin:
                inicio = datetime.strptime(fecha_inicio, '%d-%m-%Y').date()
                fin = datetime.strptime(fecha_fin, '%d-%m-%Y').date()
                queryset = queryset.filter(fecha__range=(inicio, fin))

            elif fecha_inicio:
                inicio = datetime.strptime(fecha_inicio, '%d-%m-%Y').date()
                queryset = queryset.filter(fecha__gte=inicio)

            elif fecha_fin:
                fin = datetime.strptime(fecha_fin, '%d-%m-%Y').date()
                queryset = queryset.filter(fecha__lte=fin)
            
            

        except ValueError:
            return AsistenciaDetalle.objects.none()
        
        return queryset
    
    
class AsistenciaUsuarioListView(ListAPIView):

    serializer_class = AsistenciaUsuarioSerializer


    def get_queryset(self):

        usuario = self.request.query_params.get('usuario')

        fecha_inicio = self.request.query_params.get('fecha_inicio')

        fecha_fin = self.request.query_params.get('fecha_fin')


        if not usuario:
            return Persona.objects.none()



        try:

            usuario_asistencia = UsuarioAsistencia.objects.get(
                usuario__username=usuario
            )


        except UsuarioAsistencia.DoesNotExist:

            return Persona.objects.none()



        personas = Persona.objects.filter(
            asistenciaCabecera=
            usuario_asistencia.asistenciaCabecera
        )



        resultado = []


        for persona in personas:


            asistio = 0

            fecha_asistencia = "-"



            detalle = AsistenciaDetalle.objects.filter(
                persona=persona
            )



            if fecha_inicio and fecha_fin:


                inicio = datetime.strptime(
                    fecha_inicio,
                    '%d-%m-%Y'
                ).date()


                fin = datetime.strptime(
                    fecha_fin,
                    '%d-%m-%Y'
                ).date()



                registro = detalle.filter(
                    fecha__range=(inicio, fin)
                ).first()



                if registro:

                    asistio = 1

                    fecha_asistencia = registro.fecha.strftime(
                        '%d/%m/%Y'
                    )



            resultado.append({

                "persona": persona.id,

                "persona_nombre":
                f"{persona.nombre} {persona.apellidos}",

                "codigo":
                persona.codigo,

                "fecha":
                fecha_asistencia,

                "asistio":
                asistio

            })


        return resultado
    
    
    