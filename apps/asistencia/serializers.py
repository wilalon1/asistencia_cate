from rest_framework import serializers
from .models import Persona, AsistenciaCabecera, AsistenciaDetalle

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class AsistenciaCabeceraSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaCabecera
        fields = '__all__'


class AsistenciaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaDetalle
        fields = '__all__'