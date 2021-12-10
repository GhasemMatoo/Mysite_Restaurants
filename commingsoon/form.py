from django import forms
from commingsoon.models import NEWSLETTER

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NEWSLETTER
        fields = '__all__'