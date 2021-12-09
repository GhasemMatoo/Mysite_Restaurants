from django.urls import path

from commingsoon.views import *

app_name = 'commingsoon'

urlpatterns = [
    path('', Commingsoon_views, name='commingsoon'),
]
