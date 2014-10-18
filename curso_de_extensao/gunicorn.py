# -*- coding: utf-8 -*-

import multiprocessing

reload = True
bind = "0.0.0.0:9000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = "/opt/app"
raw_env = [
    'DJANGO_SETTINGS_MODULE=curso_de_extensao.settings.production'
]
