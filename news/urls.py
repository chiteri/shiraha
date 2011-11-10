from django.conf.urls.defaults import * 
from shiraha.news.models import News 

# Create your views here.
news_info_dict = {
    'queryset': News.objects.all(),
}

urlpatterns = patterns('django.views.generic', 
    #(r'^$', 'date_based.archive_index', news_info_dict),
    (r'^$', 'list_detail.object_list', dict(news_info_dict, paginate_by=3)),
) 

news_info_dict = {
    'queryset': News.objects.all(),
    'date_field': 'pub_date',
}
urlpatterns += patterns('django.views.generic', 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'date_based.object_detail', news_info_dict),
)
