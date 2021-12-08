from django.shortcuts import render

from mysit.forms import ContactForm
from django.contrib import messages
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
            messages.add_message(request, messages.SUCCESS, 'Yor ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Yor ticket dident submited.')
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