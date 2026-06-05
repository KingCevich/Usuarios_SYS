from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Usuario, Perfil_entidad, Preferencia
import sys

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    if sender.name != 'usuarios_app':  # ← cambia por el nombre real de tu app
        return
    if 'test' in sys.argv:  
        return

    usuarios = [
        {
            "data": {
                "nombre": "Demo", "apellido": "Dueno",
                "email": "dueno@demo.com", "rut": "11111111-1",
                "telefono": "+56911111111", "password": make_password("123456"),
                "rol": "Dueno", "aprobacion_org": False,
            },
            "preferencias": True,
            "perfil_entidad": None,
        },
        {
            "data": {
                "nombre": "Demo", "apellido": "Refugio",
                "email": "refugio@demo.com", "rut": "22222222-2",
                "telefono": "+56922222222", "password": make_password("123456"),
                "rol": "Refugio", "aprobacion_org": True,
            },
            "preferencias": True,
            "perfil_entidad": {
                "nombre_entidad": "Refugio Demo",
                "telefono_entidad": "+56922222222",
                "email_entidad": "refugio@demo.com",
                "ubicacion_entidad": "Santiago, Chile",
                "descripcion_entidad": "Refugio de prueba para desarrollo.",
            },
        },
        {
            "data": {
                "nombre": "Demo", "apellido": "Veterinaria",
                "email": "veterinaria@demo.com", "rut": "33333333-3",
                "telefono": "+56933333333", "password": make_password("123456"),
                "rol": "Veterinario", "aprobacion_org": True,
            },
            "preferencias": True,
            "perfil_entidad": {
                "nombre_entidad": "Veterinaria Demo",
                "telefono_entidad": "+56933333333",
                "email_entidad": "veterinaria@demo.com",
                "ubicacion_entidad": "Providencia, Santiago",
                "descripcion_entidad": "Clínica veterinaria de prueba.",
            },
        },
        {
            "data": {
                "nombre": "Demo", "apellido": "Municipalidad",
                "email": "municipalidad@demo.com", "rut": "44444444-4",
                "telefono": "+56944444444", "password": make_password("123456"),
                "rol": "Municipalidad", "aprobacion_org": True,
            },
            "preferencias": True,
            "perfil_entidad": {
                "nombre_entidad": "Municipalidad Demo",
                "telefono_entidad": "+56944444444",
                "email_entidad": "municipalidad@demo.com",
                "ubicacion_entidad": "Las Condes, Santiago",
                "descripcion_entidad": "Municipalidad de prueba.",
            },
        },
        {
            "data": {
                "nombre": "Demo", "apellido": "Admin",
                "email": "admin@demo.com", "rut": "55555555-5",
                "telefono": "+56955555555", "password": make_password("123456"),
                "rol": "Admin", "aprobacion_org": True,
            },
            "preferencias": True,
            "perfil_entidad": None,
        },
    ]

    for u in usuarios:
        if not Usuario.objects.filter(email=u["data"]["email"]).exists():
            usuario = Usuario.objects.create(**u["data"])
            if u["preferencias"]:
                Preferencia.objects.create(usuario_preferencia=usuario)
            if u["perfil_entidad"]:
                Perfil_entidad.objects.create(usuario_perfil=usuario, **u["perfil_entidad"])
            print(f"<<<<Usuario creado: {u['data']['email']}>>>>")


@receiver(post_migrate)
def create_default_user(sender, **kwargs):  # ← el original, mantenlo si quieres
    if sender.name != 'usuarios_app':
        return
    if 'test' in sys.argv:  
        return
    if not Usuario.objects.filter(email="demo@auth.com").exists():
        u = Usuario.objects.create(
            nombre="Prueba", apellido="User",
            email="demo@auth.com", rut="11222333-4",
            telefono="+56912345678", password=make_password("123456"),
            rol="Dueno", aprobacion_org=True,
        )
        Preferencia.objects.create(usuario_preferencia=u)
        print("<<<<Usuario de prueba creado>>>>")
        
# @receiver(post_migrate)
# def create_default_user(sender, **kwargs):
#     if not Usuario.objects.filter(email="demo@auth.com").exists():
#         Usuario.objects.create(
#             nombre="Prueba",
#             apellido="User",
#             email="demo@auth.com",
#             rut="11222333-4",
#             telefono="+56912345678",
#             password= make_password("123456"), 
#             rol="Admin",
#             aprobacion_org=True
#         )
#         print("<<<<Usuario de prueba creado>>>>")

# @receiver(post_save, sender=Usuario)
# def hash_password_on_save(sender, instance, **kwargs):
#     if instance.password and not instance.password.startswith('pbkdf2_sha256$'):
#         instance.password = make_password(instance.password)
#         instance.save(update_fields=['password'])
