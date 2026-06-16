from django.shortcuts import render
from apps.asistencia.models import UsuarioAsistencia

def listar(request):
    
    usuario_asistencia = UsuarioAsistencia.objects.filter(
        usuario=request.user
    ).first()

    return render(
        request,
        'cliente/listar.html',
        {
            'usuario_asistencia': usuario_asistencia
        }
    )