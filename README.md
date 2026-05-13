# 👤 usuarios_serv

Microservicio de gestión de usuarios del sistema SanosYSalvos. Se encarga de almacenar y administrar la información de todos los usuarios registrados, sus perfiles de entidad (veterinarias, refugios) y sus preferencias de notificación.

**Puerto:** `8000`

---

## Responsabilidades

- Crear, leer, actualizar y eliminar usuarios
- Gestionar perfiles de entidades vinculadas a usuarios (veterinarias, clínicas, refugios)
- Administrar preferencias de notificación por usuario (push, email, georeporte)

---

## Modelos

### `Usuario`
Representa a un usuario registrado en el sistema.

| Campo | Tipo | Descripción |
|---|---|---|
| `nombre` | CharField | Nombre del usuario |
| `apellido` | CharField | Apellido del usuario |
| `email` | CharField | Correo electrónico (único) |
| `telefono` | CharField | Número de teléfono |
| `password` | CharField | Contraseña encriptada |
| `rol` | CharField | Rol del usuario (`Dueno`, `Admin`, etc.) |
| `is_active` | BooleanField | Estado activo/inactivo |

### `Perfil_entidad`
Perfil extendido para usuarios que representan una entidad (veterinaria, refugio).

| Campo | Tipo | Descripción |
|---|---|---|
| `usuario_perfil` | ForeignKey | Usuario al que pertenece el perfil |
| `nombre_entidad` | CharField | Nombre de la entidad |
| `telefono_entidad` | CharField | Teléfono de la entidad |
| `email_entidad` | CharField | Email de la entidad |
| `ubicacion_entidad` | CharField | Ubicación de la entidad |
| `descripcion_entidad` | TextField | Descripción de la entidad |

### `Preferencia`
Preferencias de notificación del usuario.

| Campo | Tipo | Descripción |
|---|---|---|
| `usuario_preferencia` | ForeignKey | Usuario al que pertenecen las preferencias |
| `noti_push` | BooleanField | Activar notificaciones push |
| `georeporte` | BooleanField | Activar reportes por geolocalización |
| `noti_email` | BooleanField | Activar notificaciones por email |

---

## Endpoints

| Método | URL | Descripción |
|---|---|---|
| GET | `/api/usuarios/` | Listar todos los usuarios |
| POST | `/api/usuarios/` | Crear un nuevo usuario |
| GET | `/api/usuarios/{id}/` | Obtener un usuario por ID |
| PATCH | `/api/usuarios/{id}/` | Actualizar parcialmente un usuario |
| DELETE | `/api/usuarios/{id}/` | Eliminar un usuario |
| GET | `/api/perfiles/` | Listar todos los perfiles de entidades |
| POST | `/api/perfiles/` | Crear un nuevo perfil de entidad |
| GET | `/api/preferencias/` | Listar todas las preferencias |
| POST | `/api/preferencias/` | Crear preferencias para un usuario |

> **Nota:** Se puede utilizar Thunder o Postman para las peticiones API por medio http://127.0.0.1:8000/.
---

---

## Tests

Los tests cubren tanto los modelos como la API REST:

**Tests de modelos:**
- `test_create_usuario` — Verifica que se crea correctamente un usuario con todos sus campos
- `test_create_perfil` — Verifica que se crea un perfil de entidad vinculado a un usuario
- `test_create_preferencia` — Verifica que se crean preferencias de notificación correctamente

**Tests de API:**
- `test_list_usuarios` — GET devuelve lista de usuarios con status 200
- `test_create_usuario` — POST crea un usuario y devuelve status 201
- `test_retrieve_usuario` — GET por ID devuelve el usuario correcto
- `test_update_usuario` — PATCH actualiza el nombre y persiste el cambio
- `test_delete_usuario` — DELETE elimina el usuario correctamente
- `test_list_perfiles` — GET devuelve lista de perfiles con status 200
- `test_create_perfil` — POST crea un perfil y devuelve status 201
- `test_list_preferencias` — GET devuelve lista de preferencias con status 200
- `test_create_preferencia` — POST crea preferencias y devuelve status 201
  

```bash
cd usuarios_serv
python manage.py test
```

---

## Levantar el servicio

```bash
cd usuarios_serv
python manage.py migrate
python manage.py runserver 8000
```
