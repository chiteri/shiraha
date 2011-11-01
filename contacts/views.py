from django.shortcuts import render_to_response
from django.template import RequestContext 
from shiraha.context_processors import custom_proc

# Create your views here.
def contacts(request): 
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('e-mail', 'martin.chiteri@gmail.com'),
                ['chiteri@geek.co.ke'],
            )
            return HttpResponseRedirect('/contacts/thanks/')
    return render_to_response('contacts/contact_form.html', {'errors':errors}, context_instance=RequestContext(request, processors = [custom_proc]) )
	
def thank_you(request): 
    return render_to_response('contacts/thank_you.html')
	