from django.urls import path
from . import views


app_name = "asistencia"


urlpatterns = [

    path(
        'listar/',
        views.listar,
        name='listar'
    ),

]