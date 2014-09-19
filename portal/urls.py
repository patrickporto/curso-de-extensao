from django.conf.urls import patterns, include, url

urlpatterns = patterns('portal.views',
    # Examples:
    # url(r'^$', 'escolar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'home', name='home'),
    url(r'^contato/', 'contato', name='contato'),
    url(r'^access/', 'access', name='access'),
    url(r'^logout/', 'user_logout', name='logout'),
)
