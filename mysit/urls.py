from django.urls import path
from mysit.views import *

app_name = 'mysit'


urlpatterns = [
    path('',index_views, name='index'),
    path('about',about_views, name='about'),
    path('contact',contact_views, name='contact'),
    path('gallery',gallery_views, name='gallery'),
    path('menu',menu_views, name='menu'),
    path('reservation',reservation_views, name='reservation'),
    path('stuff',stuff_views, name='stuff')
]