from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'haupt.views.index', name='index'),
    url(r'^order/', include('orderform.urls')),
    url(r'^haupt/', include('haupt.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
