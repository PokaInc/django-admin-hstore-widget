import os

import django


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_hstore',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    },
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_admin_hstore_widget',

    'tests',
)

if django.VERSION[:2] >= (1, 7):
    INSTALLED_APPS = (
                         'django.contrib.admin.apps.AdminConfig',
                     ) + INSTALLED_APPS
else:
    INSTALLED_APPS = (
                         'django.contrib.admin',
                     ) + INSTALLED_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECRET_KEY = 'secret'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
ROOT_URLCONF = 'tests.urls'

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
