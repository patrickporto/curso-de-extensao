# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('disciplina.views',
    url(r'^$', 'disciplinas', name='disciplinas'),
)
