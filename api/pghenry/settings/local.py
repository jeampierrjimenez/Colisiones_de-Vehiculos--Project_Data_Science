import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'henry',
                'USER': 'usuario_henry',
                'PASSWORD': 'henrypf',
                'HOST': '66.97.41.26',
                'PORT': '3306',
        }
}
