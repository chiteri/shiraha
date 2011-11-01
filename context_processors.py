from django.template import RequestContext 
from shiraha.news.models import News
from shiraha.project.models import Project 

def custom_proc(Request): 
    # A context processor that provides a list of latest projects and news items
    return { 'LATEST_NEWS': News.objects.all()[:4], 'LATEST_PROJECTS': Project.objects.all()[:6]}