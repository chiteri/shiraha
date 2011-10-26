from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse 
from django.template import RequestContext 
from shiraha.context_processors import custom_proc
from shiraha.news.models import News
from shiraha.project.models import Project
import datetime 

def current_datetime(request): 
    now = datetime.datetime.now() 
    html = "<html><body> <h3> It is now %s. </h3> </body></html>"%now 
    return HttpResponse (html)
	
def home(request): 
    news = News.objects.all()[:4]
    # return render_to_response('base.html', {'news':news})
    # return direct_to_template(request, 'base.html' , {'context_instance':RequestContext(request), 'news':news}) 
    return direct_to_template(request, 'base.html' , context_instance=RequestContext(request, processors = [custom_proc]))
	
def gallery(request): 
    news = News.objects.all()[:4]
    # return render_to_response('base.html', {'news':news})
    return direct_to_template(request, 'photo/gallery.html' , {'context_instance':RequestContext(request), 'news':news}) 
	