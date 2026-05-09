from django.db import models

ROL = [
    ("Dueno", "Dueno"),
    ("Colaborador", "Colaborador"),
    ("Veterinario", "Veterinario"),
    ("Refugio", "Refugio"),
    ("Municipalidad", "Municipalidad"),
    ("Admin", "Admin"),
]

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL)
    aprobacion_org = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)


    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_rol_display()}"
    
class Perfil_entidad(models.Model):
    usuario_perfil = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_entidad")
    nombre_entidad = models.CharField(max_length=100)
    telefono_entidad = models.CharField(max_length=20, blank=True, null=True)
    email_entidad = models.EmailField(blank=True, null=True)
    ubicacion_entidad = models.CharField(max_length=255, blank=True, null=True)
    descripcion_entidad = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return f"Perfil de {self.nombre_entidad} - Usuario: {self.usuario_perfil.nombre} {self.usuario_perfil.apellido}"

class Preferencia(models.Model):
    usuario_preferencia = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="preferencias")
    noti_push = models.BooleanField(default=True)
    georeporte = models.BooleanField(default=True)
    noti_email = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferencias de {self.usuario_preferencia.nombre} {self.usuario_preferencia.apellido}"
    




