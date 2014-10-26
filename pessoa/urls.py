# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from pessoa.views import documentos

urlpatterns = patterns(
    'pessoa.views',
    url(r'^pendencias/$', documentos, name='pendencias'),
)
