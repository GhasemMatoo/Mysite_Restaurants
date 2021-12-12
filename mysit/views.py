from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mysit.forms import ContactForm ,ReservationForm
from django.contrib import messages
# Create your views here.
def index_views(request):
    return render(request, 'mysit/index.html')

def about_views(request):
    return render(request, 'mysit/about.html')

def contact_views(request):
    form = ContactForm()
    return render(request, 'mysit/contact.html',{'form':form})

def gallery_views(request):
    return render(request, 'mysit/gallery.html')

def menu_views(request):
    return render(request, 'mysit/menu.html')


@login_required(login_url='/account/login')
def reservation_views(request):
    if request.method == 'POST':
        forms = ReservationForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.SUCCESS, 'Yor ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Yor ticket dident submited.')
    forms = ReservationForm()
    return render(request, 'mysit/reservation.html',{'forms':forms})

def handler404(request, exception):
    return render(request, 'mysit/index.html')