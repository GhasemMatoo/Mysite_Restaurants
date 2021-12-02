from django.shortcuts import render
from django.http import HttpResponse
from mysit.models import contact
from mysit.forms import ContactForm
# Create your views here.
def index_views(request):
    return render(request, 'mysit/index.html')

def about_views(request):
    return render(request, 'mysit/about.html')

def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("no")
    form = ContactForm()
    return render(request, 'mysit/contact.html',{'form':form})

def gallery_views(request):
    return render(request, 'mysit/gallery.html')

def menu_views(request):
    return render(request, 'mysit/menu.html')

def reservation_views(request):
    return render(request, 'mysit/reservation.html')

def stuff_views(request):
    return render(request, 'mysit/stuff.html')