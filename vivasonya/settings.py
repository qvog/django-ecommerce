from pathlib import Path
import os
import environ

# Установка локальных переменных
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "SECRET_KEY=47p-1q#wvl2cj$2!hm%l58)xd-gd3)!jtj)*e^pb73r+v6f9bn"

DEBUG = True

ALLOWED_HOSTS = ['*']

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

STRIPE_API_KEY_PUB = 'pk_test_51MRDWxGGtFrkfX6fk7pHGrOmKTA8BaooAlw8050ZyLzbtFc60A5lR159MsOUvrqNFN8XoutRPHOK9N6uzVOyrn5L00vo1f0noh'
STRIPE_API_KEY_SEC = 'sk_test_51MRDWxGGtFrkfX6fbD0fE6MKKEZtrufsGeWu7IbuXalJaf3RpWoNZcnnR6yCYHSPDBIHLjNwPi0uchWSOZTAsoGw00jedLpWOf'

#Время существования куки
SESSION_COOKIE_AGE = 87000
#ID сессии для объекта 'cart'
CART_SESSION_ID = 'cart' 


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise.runserver_nostatic',

    'core',
    'product',
    'cart',
    'order',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vivasonya.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'vivasonya.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER' : 'postgres',
        'PASSWORD' : 'dancer',
        'HOST' : '127.0.0.1',
        'PORT' : '5432',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
