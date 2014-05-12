from django.conf.urls import patterns, include, url


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'haupt.views.index', name='index'),
    url(r'^order/', include('orderform.urls')),
    url(r'^haupt/', include('haupt.urls')),
    url(r'^admin/', include(admin.site.urls)),
)




if settings.DEBUG:

    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL,

            document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()