Proyecto Django con API Rest Framework
Este proyecto es una aplicación web construida con Django y Django REST Framework. Consiste en dos aplicaciones: una para administrar propiedades y otra para administrar propietarios. Utiliza una base de datos PostgreSQL y un entorno virtual para el desarrollo.

Primeros pasos
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

Clona este repositorio en tu máquina:

bash
Copy code
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto
Crea y activa un entorno virtual:

bash
Copy code
python3 -m venv entornoVirtual
source entornoVirtual/bin/activate
Instala las dependencias del proyecto:

bash
Copy code
pip install -r requirements.txt
Configura la base de datos:

En el archivo settings.py, configura el motor de base de datos y los detalles de conexión:

python
Copy code
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
Realiza las migraciones:

bash
Copy code
python manage.py migrate
Inicia el servidor de desarrollo:

bash
Copy code
python manage.py runserver
Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

Entidades
Propiedad
La aplicación de propiedades permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre entidades de Propiedad. Puedes acceder a la API en http://127.0.0.1:8000/propiedades/.

Propietario
La aplicación de propietarios también permite operaciones CRUD sobre entidades de Propietario. La API está disponible en http://127.0.0.1:8000/propietarios/.

Solución de problemas
Configuración de CORS
Para solucionar problemas de CORS (Cross-Origin Resource Sharing), agrega las siguientes líneas a tu archivo settings.py:

python
Copy code
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Ejemplo: Cambia esto por el origen de tu frontend
    "http://127.0.0.1:9000",  # Otro ejemplo si estás usando webpack-dev-server
]
Este README es solo un ejemplo y puede ser adaptado para que se ajuste a tu proyecto específico. Asegúrate de reemplazar las URL, nombres de base de datos y otros detalles con la información correcta de tu proyecto.




