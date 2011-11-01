from django.conf.urls.defaults import * 

urlpatterns = patterns('shiraha.contacts.views', 
    (r'^$', 'contacts'),
    (r'^thanks/$', 'thank_you' ), 	
)