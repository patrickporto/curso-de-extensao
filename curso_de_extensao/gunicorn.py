# -*- encoding: utf-8 -*-
import multiprocessing

reload = True
bind = "0.0.0.0:9000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = "/opt/app"
pythonpath = "/opt/env/lib/python3.4/site-packages"
raw_env = [
    'DJANGO_SETTINGS_MODULE=escolar.settings.production'
]
