from django.conf.urls.defaults import patterns, include, url
import os.path
from django.contrib import admin
import settings
from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'egzamin.views.home', name='home'),
    # url(r'^egzamin/', include('egzamin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^egzam/$', 'egzam.views.homepage'),
     url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
     url(r'^egzam/(?P<pagenum>\d+)/$', 'egzam.views.list_egzam' ),
)