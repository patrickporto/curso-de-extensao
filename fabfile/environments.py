# -*- coding: utf-8 -*-

from fabric.api import env


def prod():
    """
    Define o ambiente das operações como sendo o de produção
    """
    env.hosts = ['104.131.39.168']
    env.user = "root"
    env.password = "projetoq1w2e3r4"
    env.key_filename = 'fabfile/deploy'
    env.DJANGO_SETTINGS = 'curso_de_extensao.settings.production'
