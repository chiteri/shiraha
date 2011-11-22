from django.views.generic.simple import direct_to_template
from django.template import RequestContext 
from shiraha.context_processors import custom_proc

def home(request): 
    return direct_to_template(request, 'base.html' , context_instance=RequestContext(request, processors = [custom_proc]))
	
def gallery(request): 
    return direct_to_template(request, 'photo/gallery.html' , {'context_instance':RequestContext(request)}) 
	