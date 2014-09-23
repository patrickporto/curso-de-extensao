from django.conf.urls import patterns, include, url

urlpatterns = patterns('downloads.views',
    url(r'^$', 'arquivos', name="arquivos"),
    url(r'^download/(?P<slug>\w*)', 'download', name="download"),
)