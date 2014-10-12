# -*- encoding: utf-8 -*-
from escolar.settings import *

ALLOWED_HOSTS = ('104.131.39.168',)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'escolar',
        'USER': 'root',
        'PASSWORD': 'e0a2201f4681784d8c2725fea98a400a40396ffa4cdbb58eb0bc7514190b6a2dec7d55d9a9c525b8b01c04d2af42713c3787bf1b40ca24a3ffd48c75ba9a97d3',
    }
}

STATIC_ROOT = '/opt/static/'
MEDIA_ROOT = '/opt/media/'
