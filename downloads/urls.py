from django.conf.urls import patterns, url

urlpatterns = patterns('downloads.views',
    url(r'^$', 'arquivos', name="arquivos"),
    url(r'^download/(?P<slug>[\w_-]*)/$', 'download', name="download"),
)