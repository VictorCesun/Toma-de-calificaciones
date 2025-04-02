from pathlib import Path
import os

# =====================
# BASE CONFIGURATION
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-*4j^s-)qe$!jgaz&nd1l9az@==@lhy^iyfrp!qw^4t=62-qo@z'
DEBUG = True
ALLOWED_HOSTS = []

# =====================
# APPLICATIONS
# =====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion_escolar',
    'rest_framework',
]

# =====================
# MIDDLEWARE
# =====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================
# URL CONFIGURATION
# =====================
ROOT_URLCONF = 'sistema_calificaciones.urls'

# =====================
# TEMPLATES CONFIGURATION
# =====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'gestion_escolar/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =====================
# WSGI CONFIGURATION
# =====================
WSGI_APPLICATION = 'sistema_calificaciones.wsgi.application'

# =====================
# DATABASE CONFIGURATION
# =====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =====================
# AUTHENTICATION & SECURITY
# =====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_REDIRECT_URL = '/redireccionar/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False  # Cambiar a True si usas HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'

# =====================
# INTERNATIONALIZATION
# =====================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =====================
# STATIC FILES CONFIGURATION
# =====================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# =====================
# DEFAULT PRIMARY KEY
# =====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'