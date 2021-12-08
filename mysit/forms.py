from django import forms
from mysit.models import contact
from captcha.fields import CaptchaField
from django_summernote.widgets import SummernoteWidget

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = ['name','subject','email','massage']
        widgets = {
            'massage': SummernoteWidget(),
        }