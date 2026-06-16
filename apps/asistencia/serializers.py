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

    persona_nombre = serializers.SerializerMethodField()


    class Meta:
        model = AsistenciaDetalle
        fields = '__all__'


    def get_persona_nombre(self, obj):

        return f"{obj.persona.nombre} {obj.persona.apellidos}"