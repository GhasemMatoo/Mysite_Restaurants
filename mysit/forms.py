from django import forms
from mysit.models import contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = contact
        fields = ['name','subject','email','massage']
