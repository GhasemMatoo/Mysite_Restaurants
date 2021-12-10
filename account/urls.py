from django.urls import path
from account.views import *

app_name = 'account'


urlpatterns = [
    path('login',login_views, name='login'),
    path('logout',logout_views, name='logout'),
    path('register',register_views, name='register'),
]