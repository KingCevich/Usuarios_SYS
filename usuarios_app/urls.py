from django.urls import path, include
from .views import (
    lista_entidades, lista_usuarios, lista_perfiles, lista_preferencias,
    UsuarioViewSet, Perfil_entidadViewSet, PreferenciaViewSet, EntidadViewSet
    #   login_user
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles', Perfil_entidadViewSet)
router.register(r'preferencias', PreferenciaViewSet)
router.register(r'entidades', EntidadViewSet)

urlpatterns = [
    # HTML 
    path('html/usuarios/', lista_usuarios, name='lista_usuarios'),
    path('html/perfiles/', lista_perfiles, name='lista_perfiles'),
    path('html/preferencias/', lista_preferencias, name='lista_preferencias'),
    path('html/entidades/', lista_entidades, name='lista_entidades'),
    # API CRUD 
    path('api/', include(router.urls)),

    # # Endpoints personalizados Prueba de Tokens
    # path('api/auth/login/', login_user, name='login_user'),
]
