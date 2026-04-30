#from django.conf.urls import url
from django.contrib.auth.views import login_required

from django.urls import path
from .views import (
    PersonaListView,
    AsistenciaCabeceraListView,
    AsistenciaDetalleListView
)

urlpatterns = [
    path('personas/', PersonaListView.as_view(), name='personas-list'),
    path('asistencia-cabecera/', AsistenciaCabeceraListView.as_view()),
    path('asistencia-detalle/', AsistenciaDetalleListView.as_view()),
]
