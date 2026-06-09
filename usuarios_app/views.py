from django.shortcuts import render
from .models import Entidad, Usuario, Perfil_entidad, Preferencia

from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import EntidadSerializer, UsuarioSerializer, Perfil_entidadSerializer, PreferenciaSerializer

from rest_framework.decorators import api_view
import jwt, time
from django.conf import settings
from django.contrib.auth.hashers import check_password
# Create your views here.

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def lista_perfiles(request):
    perfiles = Perfil_entidad.objects.all()
    return render(request, 'perfiles.html', {'perfiles': perfiles})

def lista_preferencias(request):
    preferencias = Preferencia.objects.all()
    return render(request, 'preferencias.html', {'preferencias': preferencias})

def lista_entidades(request):
    entidades = Entidad.objects.all()
    return render(request, 'entidades.html', {'entidades': entidades})

class UsuarioViewSet(viewsets.ModelViewSet):    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        queryset = Usuario.objects.all()
        email = self.request.query_params.get('email')
        if email:
            queryset = queryset.filter(email=email)
        return queryset

class Perfil_entidadViewSet(viewsets.ModelViewSet):
    queryset = Perfil_entidad.objects.all()
    serializer_class = Perfil_entidadSerializer

    def get_queryset(self):
        queryset = Perfil_entidad.objects.all()
        usuario_perfil = self.request.query_params.get('usuario_perfil')
        entidad_perfil = self.request.query_params.get('entidad_perfil')
        es_activo = self.request.query_params.get('es_activo')

        if usuario_perfil is not None:
            queryset = queryset.filter(usuario_perfil_id=usuario_perfil)
        if entidad_perfil is not None:
            queryset = queryset.filter(entidad_perfil_id=entidad_perfil)
        if es_activo is not None:
            queryset = queryset.filter(es_activo=es_activo.lower() == 'true')
        return queryset

class PreferenciaViewSet(viewsets.ModelViewSet):
    queryset = Preferencia.objects.all()
    serializer_class = PreferenciaSerializer

class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

    def get_queryset(self):
        queryset = Entidad.objects.all()
        aprobada = self.request.query_params.get('aprobacion_entidad')
        if aprobada is not None:
            queryset = queryset.filter(aprobacion_entidad=aprobada.lower() == 'true')
        return queryset

# @api_view(["POST"])
# def login_user(request):
#     email = request.data.get("email")
#     password = request.data.get("password")

#     try:
#         user = Usuario.objects.get(email=email)
#     except Usuario.DoesNotExist:
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#     # Validar contraseña encriptada
#     if not check_password(password, user.password):
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#     # Generar token si credenciales son correctas
#     now = int(time.time())
#     payload = {
#         "user_id": user.id,
#         "email": user.email,
#         "rol": user.rol,
#         "iat": now
#     }
#     token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

#     return Response({
#         "id": user.id,
#         "email": user.email,
#         "rol": user.rol,
#         "token": token
#     }, status=status.HTTP_200_OK)