from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'disciplina.views.disciplinas', name='disciplinas'),
)
