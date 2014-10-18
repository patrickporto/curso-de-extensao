# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('disciplina.views',
    url(r'^$', 'disciplinas', name='disciplinas'),
)
