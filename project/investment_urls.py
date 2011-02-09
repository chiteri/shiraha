from django.conf.urls.defaults import * 
from shiraha.project.models import Project 

investment_projects_dict = {
    'queryset': Project.investments.all(), 
    'template_name': 'project/investment_list.html',
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', investment_projects_dict), 
)

investments_dict = {
    'queryset':Project.investments.all(), 	
}

urlpatterns += patterns ('django.views.generic.list_detail', 
    (r'^(?P<slug>[-\w]+)/$', 'object_detail', investments_dict), 
)