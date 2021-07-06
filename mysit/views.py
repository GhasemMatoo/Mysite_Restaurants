from django.shortcuts import render

# Create your views here.
def index_views(request):
    return render(request, 'mysit/index.html')

def about_views(request):
    return render(request, 'mysit/about.html')

def contact_views(request):
    return render(request, 'mysit/contact.html')

def gallery_views(request):
    return render(request, 'mysit/gallery.html')

def menu_views(request):
    return render(request, 'mysit/menu.html')

def reservation_views(request):
    return render(request, 'mysit/reservation.html')

def stuff_views(request):
    return render(request, 'mysit/stuff.html')