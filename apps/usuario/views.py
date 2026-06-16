import json

from django.shortcuts import render

from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer
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