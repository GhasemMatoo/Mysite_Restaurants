from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_views, name='blog'),
    path('<int:pid>',blog_details_views, name='blog-details'),
]