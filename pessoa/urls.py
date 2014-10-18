# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('pessoa.views',
    url(r'^documentos_pendentes/$', 'documentos', name='documentos'),
)
