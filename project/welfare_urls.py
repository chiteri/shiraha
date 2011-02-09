from django.conf.urls.defaults import * 
from shiraha.project.models import Project 

welfare_projects_dict = {
    'queryset': Project.welfare.all(), 
    'template_name': 'project/welfare_list.html',
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', welfare_projects_dict), 
)

welfare_dict = {
    'queryset':Project.welfare.all(), 	
}

urlpatterns += patterns ('django.views.generic.list_detail', 
    (r'^(?P<slug>[-\w]+)/$', 'object_detail', welfare_dict), 
)