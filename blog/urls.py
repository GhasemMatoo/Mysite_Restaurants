from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_views, name='blog'),
    path('<int:pid>',blog_details_views, name='blog-details'),
    path('category/<str:cat_name>',blog_views, name='blog-category'),
    path('search/',blog_search_views, name='blog-search'),
]