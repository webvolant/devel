from django.conf.urls import patterns, url, include

from haupt import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.site, name='site'),
	url(r'^(?P<alias>[a-z]*)/$', views.site, name='site'),

)