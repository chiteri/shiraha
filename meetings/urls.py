from django.conf.urls.defaults import * 
from shiraha.meetings.models import Meeting 

meetings_info_dict = {
    'queryset': Meeting.objects.all(), 	
}

urlpatterns = patterns('django.views.generic', 
    (r'^$', 'list_detail.object_list', dict(meetings_info_dict, paginate_by=12)),
    #(r'^(?P<object_id>\d+)/details/$', 'object_detail', info_dict), 	
)

meetings_info_dict = {
    'queryset': Meeting.objects.all(), 
    'date_field': 'day_held',	
}

urlpatterns += patterns('django.views.generic', 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
	'date_based.object_detail', meetings_info_dict ), 
)