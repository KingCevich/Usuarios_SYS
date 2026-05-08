from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Usuario

@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    if not Usuario.objects.filter(email="demo@auth.com").exists():
        Usuario.objects.create(
            nombre="Prueba",
            apellido="User",
            email="demo@auth.com",
            password="123456", 
            rol="Admin",
            aprobacion_org=True
        )
        print("<<<<Usuario de prueba creado>>>>")

# def ready(self):
#     from .models import Usuario
#     from django.contrib.auth.hashers import make_password
#     if not Usuario.objects.filter(email="demo@auth.com").exists():
#         Usuario.objects.create(
#             nombre="Prueba",
#             apellido="User",
#             email="demo@auth.com",
#             password=make_password("123456"), 
#             rol="Admin",
#             aprobacion_org=True
#         )
#         print("<<<<Usuario de prueba creado>>>>")
