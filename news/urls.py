from django.conf.urls.defaults import * 
from shiraha.news.models import News 

# Create your views here.
news_info_dict = {
    'queryset': News.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based', 
    (r'^$', 'archive_index', news_info_dict),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', news_info_dict),
)
