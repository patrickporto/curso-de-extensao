from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoa.views',
    url(r'^documentos_pendentes/$', 'documentos', name='documentos'),
)
