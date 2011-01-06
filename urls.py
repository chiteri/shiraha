from django.conf.urls.defaults import * 
from shiraha.views import current_datetime, home 
import os 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^shiraha/', include('shiraha.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\','/') }), 

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)), 
    (r'^$', home),
    (r'^time/$', current_datetime ),
)
