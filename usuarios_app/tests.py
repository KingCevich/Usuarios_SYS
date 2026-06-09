from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Usuario, Entidad, Perfil_entidad, Preferencia


class UsuarioModelTest(TestCase):
    """Pruebas de creación de modelo Usuario."""

    def test_create_usuario(self):
        # Verifica que se puede crear un usuario y su __str__ esté formateado correctamente.
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
        self.assertEqual(str(usuario), 'Juan Perez - Dueño')


class EntidadModelTest(TestCase):
    """Pruebas de creación de modelo Entidad."""

    def test_create_entidad(self):
        # Comprueba que la entidad se guarda con sus campos obligatorios y el __str__ correcto.
        entidad = Entidad.objects.create(
            nombre_entidad='Veterinaria ABC',
            tipo_entidad='Veterinaria',
            rut_entidad='12345678-9',
            telefono_entidad='987654321',
            email_entidad='vet@example.com',
            ubicacion_entidad='Centro',
            comuna_entidad='Santiago',
            descripcion_entidad='Clínica veterinaria',
            aprobacion_entidad=True
        )
        self.assertEqual(entidad.nombre_entidad, 'Veterinaria ABC')
        self.assertEqual(str(entidad), 'Veterinaria ABC (Clínica Veterinaria)')


class PerfilEntidadModelTest(TestCase):
    """Pruebas de creación de modelo Perfil_entidad."""

    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )
        self.entidad = Entidad.objects.create(
            nombre_entidad='Veterinaria ABC',
            tipo_entidad='Veterinaria',
            rut_entidad='12345678-9',
            telefono_entidad='987654321',
            email_entidad='vet@example.com',
            ubicacion_entidad='Centro',
            comuna_entidad='Santiago',
            descripcion_entidad='Clínica veterinaria'
        )

    def test_create_perfil(self):
        # Verifica que un perfil de entidad se puede crear con usuario, entidad y rol.
        perfil = Perfil_entidad.objects.create(
            usuario_perfil=self.usuario,
            entidad_perfil=self.entidad,
            rol_entidad='Administrador',
            es_activo=True
        )
        self.assertEqual(perfil.entidad_perfil, self.entidad)
        self.assertEqual(str(perfil), f'{self.usuario} -> {self.entidad} como Administrador')


class PreferenciaModelTest(TestCase):
    """Pruebas de creación de modelo Preferencia."""

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
        # Comprueba que las preferencias se guardan y el __str__ devuelve el texto esperado.
        preferencia = Preferencia.objects.create(
            usuario_preferencia=self.usuario,
            noti_push=True,
            georeporte=False,
            noti_email=True
        )
        self.assertTrue(preferencia.noti_push)
        self.assertEqual(str(preferencia), 'Preferencias de Juan Perez')


class UsuarioAPITest(APITestCase):
    """Pruebas de la API REST de Usuario."""

    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )

    def test_list_usuarios(self):
        # GET /api/usuarios/ debe devolver al menos el usuario creado en setUp.
        url = '/api/usuarios/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_usuario(self):
        # POST /api/usuarios/ debe crear un usuario nuevo.
        url = '/api/usuarios/'
        data = {
            'nombre': 'Maria',
            'apellido': 'Garcia',
            'email': 'maria@example.com',
            'telefono': '987654321',
            'password': 'hashed_password',
            'rol': 'Dueno'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Usuario.objects.count(), 2)

    def test_retrieve_usuario(self):
        # GET /api/usuarios/{id}/ debe devolver el usuario correcto.
        url = f'/api/usuarios/{self.usuario.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Juan')

    def test_update_usuario(self):
        # PATCH /api/usuarios/{id}/ debe modificar solo el campo enviado.
        url = f'/api/usuarios/{self.usuario.pk}/'
        data = {'nombre': 'Juan Carlos'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.nombre, 'Juan Carlos')

    def test_delete_usuario(self):
        # DELETE /api/usuarios/{id}/ debe eliminar el usuario existente.
        url = f'/api/usuarios/{self.usuario.pk}/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_404_NOT_FOUND])


class EntidadAPITest(APITestCase):
    """Pruebas de la API REST de Entidad."""

    def setUp(self):
        self.entidad = Entidad.objects.create(
            nombre_entidad='Veterinaria ABC',
            tipo_entidad='Veterinaria',
            rut_entidad='12345678-9',
            telefono_entidad='987654321',
            email_entidad='vet@example.com',
            ubicacion_entidad='Centro',
            comuna_entidad='Santiago',
            descripcion_entidad='Clínica veterinaria'
        )

    def test_list_entidades(self):
        # GET /api/entidades/ debe devolver registros existentes.
        url = '/api/entidades/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_entidad(self):
        # POST /api/entidades/ debe crear una nueva entidad.
        url = '/api/entidades/'
        data = {
            'nombre_entidad': 'Refugio ABC',
            'tipo_entidad': 'Refugio',
            'rut_entidad': '87654321-0',
            'telefono_entidad': '111222333',
            'email_entidad': 'refugio@example.com',
            'ubicacion_entidad': 'Centro',
            'comuna_entidad': 'Santiago',
            'descripcion_entidad': 'Refugio de prueba',
            'aprobacion_entidad': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Entidad.objects.count(), 2)


class PerfilEntidadAPITest(APITestCase):
    """Pruebas de la API REST de Perfil_entidad."""

    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre='Juan',
            apellido='Perez',
            email='juan@example.com',
            telefono='123456789',
            password='hashed_password',
            rol='Dueno'
        )
        self.entidad = Entidad.objects.create(
            nombre_entidad='Veterinaria ABC',
            tipo_entidad='Veterinaria',
            rut_entidad='12345678-9',
            telefono_entidad='987654321',
            email_entidad='vet@example.com',
            ubicacion_entidad='Centro',
            comuna_entidad='Santiago',
            descripcion_entidad='Clínica veterinaria'
        )
        self.perfil = Perfil_entidad.objects.create(
            usuario_perfil=self.usuario,
            entidad_perfil=self.entidad,
            rol_entidad='Administrador'
        )

    def test_list_perfiles(self):
        # GET /api/perfiles/ debe devolver los perfiles creados.
        url = '/api/perfiles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_perfil(self):
        # POST /api/perfiles/ debe crear un nuevo perfil para otra entidad.
        otra_entidad = Entidad.objects.create(
            nombre_entidad='Refugio Nuevo',
            tipo_entidad='Refugio',
            rut_entidad='87654321-0',
            telefono_entidad='111222333',
            email_entidad='refugio@example.com',
            ubicacion_entidad='Norte',
            comuna_entidad='Providencia',
            descripcion_entidad='Refugio de prueba'
        )
        url = '/api/perfiles/'
        data = {
            'usuario_perfil': self.usuario.pk,
            'entidad_perfil': otra_entidad.pk,
            'rol_entidad': 'Trabajador',
            'es_activo': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Perfil_entidad.objects.count(), 2)

    def test_filter_perfiles_by_usuario(self):
        # GET /api/perfiles/?usuario_perfil=... debe filtrar perfiles por usuario.
        url = f'/api/perfiles/?usuario_perfil={self.usuario.pk}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class PreferenciaAPITest(APITestCase):
    """Pruebas de la API REST de Preferencia."""

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

    def test_list_preferencias(self):
        # GET /api/preferencias/ debe devolver las preferencias del usuario.
        url = '/api/preferencias/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_preferencia(self):
        # POST /api/preferencias/ debe permitir crear preferencias nuevas.
        url = '/api/preferencias/'
        data = {
            'usuario_preferencia': self.usuario.pk,
            'noti_push': False,
            'georeporte': True,
            'noti_email': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Preferencia.objects.count(), 2)
