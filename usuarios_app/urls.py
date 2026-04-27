from django.urls import path, include
from .views import lista_usuarios, lista_perfiles, lista_preferencias, UsuarioViewSet, Perfil_entidadViewSet, PreferenciaViewSet
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles', Perfil_entidadViewSet)
router.register(r'preferencias', PreferenciaViewSet)

urlpatterns = [
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('perfiles/', lista_perfiles, name='lista_perfiles'),   
    path('preferencias/', lista_preferencias, name='lista_preferencias'),
    path('api/', include(router.urls)),
]