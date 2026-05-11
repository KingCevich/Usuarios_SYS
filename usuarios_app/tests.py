from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Usuario, Perfil_entidad, Preferencia


class UsuarioModelTest(TestCase):
    # Prueba la creación de un objeto Usuario con todos los campos requeridos
    def test_create_usuario(self):
        usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno',
            is_active=True
        )
        self.assertEqual(usuario.nombre, 'Juan')
        self.assertEqual(str(usuario), 'Juan Perez - Dueno')


class PerfilEntidadModelTest(TestCase):
    # Prueba la creación de un perfil de entidad vinculado a un usuario
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )

    def test_create_perfil(self):
        perfil = Perfil_entidad.objects.create(
            usuario_perfil=self.usuario,
            nombre_entidad='Veterinaria ABC',
            telefono_entidad='987654321',
            email_entidad='vet@example.com',
            ubicacion_entidad='Centro',
            descripcion_entidad='Clinica veterinaria'
        )
        self.assertEqual(perfil.nombre_entidad, 'Veterinaria ABC')
        self.assertEqual(str(perfil), 'Perfil de Veterinaria ABC - Usuario: Juan Perez')


class PreferenciaModelTest(TestCase):
    # Prueba la creación de preferencias de notificación de un usuario
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )

    def test_create_preferencia(self):
        preferencia = Preferencia.objects.create(
            usuario_preferencia=self.usuario,
            noti_push=True,
            georeporte=False,
            noti_email=True
        )
        self.assertTrue(preferencia.noti_push)
        self.assertEqual(str(preferencia), 'Preferencias de Juan Perez')


class UsuarioAPITest(APITestCase):
    # Tests de API REST para operaciones CRUD de Usuarios
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )

    # Obtiene la lista de todos los usuarios (GET /api/usuarios/)
    def test_list_usuarios(self):
        url = '/api/usuarios/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Crea un nuevo usuario via POST
    def test_create_usuario(self):
        url = '/api/usuarios/'
        data = {
            'nombre': 'Maria',
            'apellido': 'Garcia',
            'email': 'maria@example.com',
            'telefono': '987654321',
            'password': 'hashed_password',
            'rol': 'Dueno'
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Usuario.objects.count(), 2)

    # Obtiene los detalles de un usuario específico por ID
    def test_retrieve_usuario(self):
        url = f'/api/usuarios/{self.usuario.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Juan')


    # Actualiza el nombre de un usuario (PATCH /api/usuarios/{id}/)
    def test_update_usuario(self):
        url = f'/api/usuarios/{self.usuario.pk}/'
        data = {'nombre': 'Juan Carlos'}
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.nombre, 'Juan Carlos')


    # Elimina un usuario (DELETE /api/usuarios/{id}/)
    def test_delete_usuario(self):
        url = f'/api/usuarios/{self.usuario.pk}/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_404_NOT_FOUND])


class PerfilEntidadAPITest(APITestCase):
    # Tests de API REST para operaciones CRUD de Perfiles de Entidades
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )
        self.perfil = Perfil_entidad.objects.create(
            usuario_perfil=self.usuario,
            nombre_entidad='Veterinaria ABC',
            telefono_entidad='987654321'
        )


    # Obtiene la lista de todos los perfiles de entidades
    def test_list_perfiles(self):
        url = '/api/perfiles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Crea un nuevo perfil de entidad via POST
    def test_create_perfil(self):
        url = '/api/perfiles/'
        data = {
            'usuario_perfil': self.usuario.pk,
            'nombre_entidad': 'Clinica XYZ',
            'telefono_entidad': '111111111'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Perfil_entidad.objects.count(), 2)


class PreferenciaAPITest(APITestCase):
    # Tests de API REST para operaciones CRUD de Preferencias
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )
        self.preferencia = Preferencia.objects.create(
            usuario_preferencia=self.usuario,
            noti_push=True,
            georeporte=True
        )


    # Obtiene la lista de todas las preferencias de usuarios
    def test_list_preferencias(self):
        url = '/api/preferencias/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Crea nuevas preferencias de notificación para un usuario via POST
    def test_create_preferencia(self):
        url = '/api/preferencias/'
        data = {
            'usuario_preferencia': self.usuario.pk,
            'noti_push': False,
            'georeporte': True,
            'noti_email': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Preferencia.objects.count(), 2)
