from rest_framework import serializers
from .models import Usuario, Perfil_entidad, Preferencia

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class Perfil_entidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil_entidad
        fields = '__all__'

class PreferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = '__all__'