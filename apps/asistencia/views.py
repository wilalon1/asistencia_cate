from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.generics import ListAPIView

from apps.asistencia.models import Persona, AsistenciaCabecera, AsistenciaDetalle

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
    queryset = AsistenciaDetalle.objects.all()
    serializer_class = AsistenciaDetalleSerializer