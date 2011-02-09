from django.conf.urls.defaults import * 
from shiraha.meetings.models import Meeting 

meetings_info_dict = {
    'queryset': Meeting.objects.all(), 
    'date_field': 'day_held',	
}

urlpatterns = patterns('django.views.generic.date_based', 
    (r'^$', 'archive_index', meetings_info_dict),
    (r'^(?P<year>\d{4})/$', 'archive_year', meetings_info_dict ),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', meetings_info_dict ),
    # (r'^(?P<year>\d{4}/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', meetings_info_dict ),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', 
	meetings_info_dict ),  
    #(r'^(?P<object_id>\d+)/details/$', 'object_detail', info_dict), 	
)