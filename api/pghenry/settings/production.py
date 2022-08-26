import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['vps-2671696-x.dattaweb.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'henry',
                'USER': 'usuario_henry',
                'PASSWORD': 'henrypf',
                'HOST': '127.0.0.1',
                'PORT': '3306',
        }
}