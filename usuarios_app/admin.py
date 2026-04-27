from django.contrib import admin
from .models import Perfil_entidad, Usuario,  Preferencia

admin.site.register(Usuario)
admin.site.register(Perfil_entidad)
admin.site.register(Preferencia)

# Register your models here.
