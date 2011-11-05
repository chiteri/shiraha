from django.shortcuts import render_to_response
from django.template import RequestContext 
from shiraha.context_processors import custom_proc
from shiraha.contacts.forms import ContactForm

# Create your views here.
def contacts(request): 
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('e_mail', 'martin.chiteri@gmail.com'),
                ['chiteri@geek.co.ke'],
            )
            return HttpResponseRedirect('/contacts/thanks/')
    else: 
        form = ContactForm()
    return render_to_response('contacts/contact_form.html', {'form':form}, context_instance=RequestContext(request, processors = [custom_proc]) )
	
def thank_you(request): 
    return render_to_response('contacts/thank_you.html')
	