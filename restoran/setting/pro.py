from restoran.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y8rxn89e_f=0vl1%%y9rj)-8gopf&+as7t@k(9vl0ckv-y+(kq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# django_sites_config
SITE_ID = 2
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#QZZyraTWhvNnA3b
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Config databases sql
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'repairir_Restoran',
        'USER': 'repairir_Restoran 	',
        'PASSWORD': 'QZZyraTWhvNnA3b',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
'''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# SECURITY Config
X_FRAME_OPTIONS = "SAMEORIGIN"
