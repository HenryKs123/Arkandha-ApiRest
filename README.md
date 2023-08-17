Proyecto Django con API Rest Framework

Este proyecto es una aplicación web construida con Django y Django REST Framework. Consiste en dos aplicaciones: una para administrar propiedades y otra para administrar propietarios. Utiliza una base de datos PostgreSQL y un entorno virtual para el desarrollo.

Primeros pasos

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. Clona este repositorio en tu máquina:

   git clone https://github.com/tu-usuario/tu-proyecto.git
   cd tu-proyecto

2. Crea y activa un entorno virtual:

   python3 -m venv entornoVirtual
   source entornoVirtual/bin/activate

3. Instala las dependencias del proyecto:

   pip install -r requirements.txt

4. Configura la base de datos:
   
   En el archivo `settings.py`, configura el motor de base de datos y los detalles de conexión:

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'nombreBaseDatos',
           'USER': 'postgres',
           'PASSWORD': '123456',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }

5. Realiza las migraciones:

   python manage.py migrate

6. Inicia el servidor de desarrollo:

   python manage.py runserver

7. Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

Endpoints

A continuación, se detallan los endpoints disponibles en la aplicación:

- Propiedad:
  - Obtener todas las propiedades: `http://127.0.0.1:8000/Propiedad/Propiedad/get/`
  - Obtener detalles de una propiedad: `http://127.0.0.1:8000/Propiedad/Propiedad/{id}/`
  - Crear una nueva propiedad: `http://127.0.0.1:8000/Propiedad/Propiedad/post/`
  - Actualizar una propiedad: `http://127.0.0.1:8000/Propiedad/Propiedad/{id}/put/`
  - Eliminar una propiedad: `http://127.0.0.1:8000/Propiedad/Propiedad/{id}/delete/`

- Propietario:
  - Obtener todos los propietarios: `http://127.0.0.1:8000/Propietario/Propietario/get/`
  - Obtener detalles de un propietario: `http://127.0.0.1:8000/Propietario/Propietario/{id}/`
  - Crear un nuevo propietario: `http://127.0.0.1:8000/Propietario/Propietario/post/`
  - Actualizar un propietario: `http://127.0.0.1:8000/Propietario/Propietario/{id}/put/`
  - Eliminar un propietario: `http://127.0.0.1:8000/Propietario/Propietario/{id}/delete/`

Solución de problemas

Configuración de CORS

Para solucionar problemas de CORS (Cross-Origin Resource Sharing), agrega las siguientes líneas a tu archivo `settings.py`:

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Ejemplo: Cambia esto por el origen de tu frontend
    "http://127.0.0.1:9000",  # Otro ejemplo si estás usando webpack-dev-server
]

