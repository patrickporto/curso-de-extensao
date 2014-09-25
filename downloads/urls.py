from django.conf.urls import patterns, url

urlpatterns = patterns('downloads.views',
    url(r'^$', 'arquivos', name="arquivos"),
    url(r'^download/(?P<slug>[\w_-]*)/$', 'download', name="download"),
    url(r'^info/(?P<slug>[\w_-]*)/$', 'info', name="arquivo_info"),
    url(r'^history/(?P<slug>[\w_-]*)/$', 'history', name="arquivo_history"),
)