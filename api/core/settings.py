from pathlib import Path
from dynaconf import settings as dynaconf_settings

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = "django-insecure-6cxh%-rukp8zir=2s$255s3rlxfe&i293s$et+t5j28d$5k%60"
DEBUG = True
ALLOWED_HOSTS = []

# Applications
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_q",
]

MY_APPS = [
    "apps.tokens",
    "apps.emails",
]

INSTALLED_APPS = [] + DJANGO_APPS + MY_APPS

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL Configuration
ROOT_URLCONF = "core.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Adicione seu diretório de templates aqui
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# QCluster
Q_CLUSTER = {
    'name': 'DjangoQCluster',
    'workers': 4,
    'recycle': 500,
    'timeout': 60,
    'ack_failures': True,
    'retry': 120,
    'orm': 'default',
    'sync': False,
    'catch_up': False,
    'max_attempts': 1,
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'password': None,
        'socket_timeout': None,
        'charset': 'utf-8',
        'errors': 'strict',
    }
}


# WSGI Application
WSGI_APPLICATION = "core.wsgi.application"

# Database
DATABASES = {
    'default': {
        'ENGINE': dynaconf_settings.DB_ENGINE,
        'NAME': dynaconf_settings.DB_NAME,
        'USER': dynaconf_settings.DB_USER,
        'PASSWORD': dynaconf_settings.DB_PASSWORD,
        'HOST': dynaconf_settings.DB_HOST,
        'PORT': dynaconf_settings.DB_PORT,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes;',
        },
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Para adicionar diretórios estáticos adicionais

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Custom user model
# AUTH_USER_MODEL = "myapp.MyUser"  # Descomente e ajuste caso use um modelo de usuário customizado

# Logging (opcional)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
