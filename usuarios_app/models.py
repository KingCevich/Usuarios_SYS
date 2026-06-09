from django.db import models


ROL_ENTIDAD = [
        ("Administrador", "Administrador de entidad"),
        ("Trabajador", "Trabajador/Empleado")
    ]

TIPO_ENTIDAD = [
        ("Refugio", "Refugio"),
        ("Municipalidad", "Municipalidad"),
        ("Veterinaria", "Clínica Veterinaria")
    ]

ROL = [
    ("Dueno", "Dueño"),
    ("Colaborador", "Colaborador"),
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
    is_active = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_rol_display()}"

class Entidad(models.Model):
    nombre_entidad = models.CharField(max_length=100)
    tipo_entidad = models.CharField(max_length=20, choices=TIPO_ENTIDAD)
    rut_entidad = models.CharField(max_length=12, unique=True)
    telefono_entidad = models.CharField(max_length=20, blank=True, null=True)
    email_entidad = models.EmailField()
    ubicacion_entidad = models.CharField(max_length=255)
    comuna_entidad = models.CharField(max_length=100)
    descripcion_entidad = models.TextField(blank=True, null=True)
    aprobacion_entidad = models.BooleanField(default=False)
    fecha_creacion_entidad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_entidad} ({self.get_tipo_entidad_display()})"

    
class Perfil_entidad(models.Model):
    usuario_perfil = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_entidad")
    entidad_perfil = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name="perfil_entidad", null=True, blank=True)
    rol_entidad = models.CharField(max_length=20, choices=ROL_ENTIDAD, null=True, blank=True)
    es_activo = models.BooleanField(default=True)
    fecha_ingreso_perfil = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        unique_together = ('usuario_perfil', 'entidad_perfil')

    def __str__(self):
        return f"{self.usuario_perfil} -> {self.entidad_perfil} como {self.rol_entidad}"


class Preferencia(models.Model):
    usuario_preferencia = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="preferencias")
    noti_push = models.BooleanField(default=True)
    georeporte = models.BooleanField(default=True)
    noti_email = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferencias de {self.usuario_preferencia.nombre} {self.usuario_preferencia.apellido}"
    




