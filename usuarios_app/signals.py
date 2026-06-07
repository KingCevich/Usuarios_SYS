from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Usuario, Entidad, Perfil_entidad, Preferencia
import sys

@receiver(post_migrate)
def create_default_users(sender, **kwargs):
    if sender.name != 'usuarios_app':  # ajusta al nombre real de tu app
        return
    if 'test' in sys.argv:
        return

    # 1. Dueño
    if not Usuario.objects.filter(email="dueno@demo.com").exists():
        dueno = Usuario.objects.create(
            nombre="Demo", apellido="Dueño",
            email="dueno@demo.com", rut="11111111-1",
            telefono="+56911111111", password=make_password("123456"),
            rol="Dueno"
        )
        Preferencia.objects.create(usuario_preferencia=dueno)
        print("<<<<Usuario creado: dueno@demo.com>>>>")

    # 2. Refugio
    if not Usuario.objects.filter(email="refugio@demo.com").exists():
        admin_refugio = Usuario.objects.create(
            nombre="Admin", apellido="Refugio",
            email="refugio@demo.com", rut="22222222-2",
            telefono="+56922222222", password=make_password("123456"),
            rol="Colaborador"
        )
        Preferencia.objects.create(usuario_preferencia=admin_refugio)

        entidad_refugio = Entidad.objects.create(
            nombre_entidad="Refugio Demo",
            tipo_entidad="Refugio",
            rut_entidad="22222222-2",
            email_entidad="refugio@demo.com",
            ubicacion_entidad="Santiago, Chile",
            comuna_entidad="Santiago",
            telefono_entidad="+56922222222",
            descripcion_entidad="Refugio de prueba para desarrollo.",
            aprobacion_entidad=True
        )
        Perfil_entidad.objects.create(
            usuario_perfil=admin_refugio,
            entidad_perfil=entidad_refugio,
            rol_entidad="Administrador"
        )
        print("<<<<Usuario y entidad creados: refugio@demo.com>>>>")

    # 3. Veterinaria
    if not Usuario.objects.filter(email="veterinaria@demo.com").exists():
        admin_vet = Usuario.objects.create(
            nombre="Admin", apellido="Veterinaria",
            email="veterinaria@demo.com", rut="33333333-3",
            telefono="+56933333333", password=make_password("123456"),
            rol="Colaborador"
        )
        Preferencia.objects.create(usuario_preferencia=admin_vet)

        entidad_vet = Entidad.objects.create(
            nombre_entidad="Veterinaria Demo",
            tipo_entidad="Veterinaria",
            rut_entidad="33333333-3",
            email_entidad="veterinaria@demo.com",
            ubicacion_entidad="Providencia, Santiago",
            comuna_entidad="Providencia",
            telefono_entidad="+56933333333",
            descripcion_entidad="Clínica veterinaria de prueba.",
            aprobacion_entidad=True
        )
        Perfil_entidad.objects.create(
            usuario_perfil=admin_vet,
            entidad_perfil=entidad_vet,
            rol_entidad="Administrador"
        )
        print("<<<<Usuario y entidad creados: veterinaria@demo.com>>>>")

    # 4. Municipalidad
    if not Usuario.objects.filter(email="municipalidad@demo.com").exists():
        admin_muni = Usuario.objects.create(
            nombre="Admin", apellido="Municipalidad",
            email="municipalidad@demo.com", rut="44444444-4",
            telefono="+56944444444", password=make_password("123456"),
            rol="Colaborador"
        )
        Preferencia.objects.create(usuario_preferencia=admin_muni)

        entidad_muni = Entidad.objects.create(
            nombre_entidad="Municipalidad Demo",
            tipo_entidad="Municipalidad",
            rut_entidad="44444444-4",
            email_entidad="municipalidad@demo.com",
            ubicacion_entidad="Las Condes, Santiago",
            comuna_entidad="Las Condes",
            telefono_entidad="+56944444444",
            descripcion_entidad="Municipalidad de prueba.",
            aprobacion_entidad=True
        )
        Perfil_entidad.objects.create(
            usuario_perfil=admin_muni,
            entidad_perfil=entidad_muni,
            rol_entidad="Administrador"
        )
        print("<<<<Usuario y entidad creados: municipalidad@demo.com>>>>")

    # 5. Admin de plataforma
    if not Usuario.objects.filter(email="admin@demo.com").exists():
        admin_plat = Usuario.objects.create(
            nombre="Super", apellido="Admin",
            email="admin@demo.com", rut="55555555-5",
            telefono="+56955555555", password=make_password("123456"),
            rol="Admin"
        )
        Preferencia.objects.create(usuario_preferencia=admin_plat)
        print("<<<<Usuario creado: admin@demo.com>>>>")

    # 6. Colaborador Sanos y Salvos (sin entidad)
    if not Usuario.objects.filter(email="colaborador@demo.com").exists():
        colab = Usuario.objects.create(
            nombre="Colaborador", apellido="Sanos y Salvos",
            email="colaborador@demo.com", rut="66666666-6",
            telefono="+56966666666", password=make_password("123456"),
            rol="Colaborador"
        )
        Preferencia.objects.create(usuario_preferencia=colab)
        print("<<<<Usuario creado: colaborador@demo.com>>>>")

    # 7. Usuario de prueba genérico
    if not Usuario.objects.filter(email="demo@auth.com").exists():
        u = Usuario.objects.create(
            nombre="Prueba", apellido="User",
            email="demo@auth.com", rut="11222333-4",
            telefono="+56912345678", password=make_password("123456"),
            rol="Dueno"
        )
        Preferencia.objects.create(usuario_preferencia=u)
        print("<<<<Usuario de prueba creado: demo@auth.com>>>>")