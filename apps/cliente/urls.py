from django.urls import path
from . import views


app_name = "cliente"


urlpatterns = [

    path(
        'listar/',
        views.listar,
        name='listar'
    ),

]