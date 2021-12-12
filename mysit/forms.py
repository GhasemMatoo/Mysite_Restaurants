from django.forms import ModelForm
from mysit.models import contact, Reservation
from captcha.fields import CaptchaField
from django_summernote.widgets import SummernoteWidget


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = contact
        fields = ['name', 'subject', 'email', 'massage']
        widgets = {
            'massage': SummernoteWidget(),
        }


class ReservationForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Reservation
        fields = ['name', 'subject', 'email','theme','number_people','phone_number', 'massage']
        widgets = {
            'massage': SummernoteWidget(),
        }