from django.shortcuts import render
from .models import Usuario, Perfil_entidad, Preferencia

from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import UsuarioSerializer, Perfil_entidadSerializer, PreferenciaSerializer
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

class UsuarioViewSet(viewsets.ModelViewSet):    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Perfil_entidadViewSet(viewsets.ModelViewSet):
    queryset = Perfil_entidad.objects.all()
    serializer_class = Perfil_entidadSerializer 

class PreferenciaViewSet(viewsets.ModelViewSet):
    queryset = Preferencia.objects.all()
    serializer_class = PreferenciaSerializer