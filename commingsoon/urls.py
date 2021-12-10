from django.urls import path ,re_path
from commingsoon.views import *

app_name = 'commingsoon'

urlpatterns = [
    re_path(r"^", Commingsoon_views, name='commingsoon'),
    #re_path(r"^",ALL_view, name="all"),
]
