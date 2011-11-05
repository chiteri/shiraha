from django import forms 

class ContactForm(forms.Form): 
    subject = forms.CharField() 
    e_mail = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea) 