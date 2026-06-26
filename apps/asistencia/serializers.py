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
    
    def get_asistio(self, obj):

        return getattr(obj, 'asistio', 0)
    
class AsistenciaUsuarioSerializer(serializers.Serializer):

    persona = serializers.IntegerField()

    persona_nombre = serializers.CharField()

    codigo = serializers.CharField()
    
    fecha = serializers.CharField()

    asistio = serializers.CharField()