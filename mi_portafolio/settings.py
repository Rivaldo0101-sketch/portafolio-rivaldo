import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# En la computadora muestra los errores.
# En Render se desactiva automáticamente.
DEBUG = 'RENDER' not in os.environ

# La clave de internet se configurará dentro de Render.
if DEBUG:
    SECRET_KEY = 'clave-solo-para-desarrollo-local-del-portafolio'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Agrega la dirección que Render asigne al sitio.
direccion_render = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if direccion_render:
    ALLOWED_HOSTS.append(direccion_render)

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'portafolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_portafolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_portafolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_TZ = True

# Estilos, JavaScript e imágenes.
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'