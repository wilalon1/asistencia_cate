from django.urls import path


from .views import (
    PersonaListView,
    AsistenciaCabeceraListView,
    AsistenciaDetalleListView,
    PersonaPorUsuarioListView,
    AsistenciaUsuarioListView,
)


urlpatterns = [

    path(
        'personas/',
        PersonaListView.as_view()
    ),

    path(
        'asistencia-cabecera/',
        AsistenciaCabeceraListView.as_view()
    ),


    path(
        'asistencia-detalle/',
        AsistenciaDetalleListView.as_view()
    ),


    path(
        'personas/filtro',
        PersonaPorUsuarioListView.as_view()
    ),
    
    path(
        'asistencia-usuario/',
        AsistenciaUsuarioListView.as_view()
    ),


]