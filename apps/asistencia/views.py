from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.generics import ListAPIView
from datetime import datetime  # 👈 IMPORTANTE

from apps.asistencia.models import Persona, AsistenciaCabecera, AsistenciaDetalle

#Filtros de pruebas
#http://127.0.0.1:8000/api/asistencia-detalle/?fecha_inicio=01-04-2026&fecha_fin=01-04-2026
#http://127.0.0.1:8000/api/asistencia-detalle/?cabecera_id=1&fecha_inicio=01-04-2026&fecha_fin=30-04-2026
#http://127.0.0.1:8000/api/asistencia-detalle/?cabecera_id=1

from .serializers import (
    PersonaSerializer,
    AsistenciaCabeceraSerializer,
    AsistenciaDetalleSerializer
)

class PersonaListView(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class AsistenciaCabeceraListView(ListAPIView):
    queryset = AsistenciaCabecera.objects.all()
    serializer_class = AsistenciaCabeceraSerializer


class AsistenciaDetalleListView(ListAPIView):
    serializer_class = AsistenciaDetalleSerializer

    def get_queryset(self):
        queryset = AsistenciaDetalle.objects.all()

        # 🔹 parámetros
        cabecera_id = self.request.query_params.get('cabecera_id')
        persona_id = self.request.query_params.get('idPersona')
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')
        observacion = self.request.query_params.get('observacion')  # 👈 NUEVO

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