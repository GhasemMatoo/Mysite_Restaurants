from django import forms
from commingsoon.models import NEWSLETTER
from captcha.fields import CaptchaField

class NewsletterForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = NEWSLETTER
        fields = '__all__'