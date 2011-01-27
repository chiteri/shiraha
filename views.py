from django.shortcuts import render_to_response 
from django.http import HttpResponse 
import datetime 

def current_datetime(request): 
    now = datetime.datetime.now() 
    html = "<html><body> <h3> It is now %s. </h3> </body></html>"%now 
    return HttpResponse (html)
	
def home(request): 
    return render_to_response('base.html')