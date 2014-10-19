# -*- coding: utf-8 -*-

from curso_de_extensao.settings import *

ALLOWED_HOSTS = ('104.131.39.168',)

DEBUG = True

DB_USER = 'cursodeextensao'
DB_PASSWORD = '#!Q@W#E$R'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cursodeextensao',
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

STATIC_ROOT = '/opt/static/'
MEDIA_ROOT = '/opt/media/'
