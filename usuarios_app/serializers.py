from rest_framework import serializers
from .models import Usuario, Perfil_entidad, Preferencia
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get("password")
        if password:
            validated_data["password"] = make_password(password)  # encripta
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        if password:
            validated_data["password"] = make_password(password)  #  encripta
        return super().update(instance, validated_data)

class Perfil_entidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil_entidad
        fields = '__all__'

class PreferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferencia
        fields = '__all__'