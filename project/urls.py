from django.conf.urls.defaults import * 
from shiraha.project.models import Project 

projects_dict = {
    'queryset': Project.objects.all(), 
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', projects_dict), 
    (r'^(?P<slug>[-\w]+)/$', 'object_detail', projects_dict), 
)