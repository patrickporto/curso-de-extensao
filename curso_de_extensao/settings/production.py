# -*- encoding: utf-8 -*-
from curso_de_extensao.settings import *

ALLOWED_HOSTS = ('104.131.39.168',)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cursodeextensao',
        'USER': 'escola',
        'PASSWORD': '#!Q@W#E$R',
    }
}

STATIC_ROOT = '/opt/static/'
MEDIA_ROOT = '/opt/media/'
