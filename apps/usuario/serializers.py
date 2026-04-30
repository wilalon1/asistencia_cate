from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Persona, AsistenciaCabecera, AsistenciaDetalle


class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('first_name', 'email')

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class AsistenciaCabeceraSerializer(ModelSerializer):
    class Meta:
        model = AsistenciaCabecera
        fields = '__all__'


class AsistenciaDetalleSerializer(ModelSerializer):
    class Meta:
        model = AsistenciaDetalle
        fields = '__all__'