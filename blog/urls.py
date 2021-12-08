from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',blog_views, name='blog'),
    path('<int:pid>',blog_details_views, name='blog-details'),
    path("Tag/<str:tag_name>", blog_views, name='blog-tags'),
    path('category/<str:cat_name>',blog_views, name='blog-category'),
    path("author/<str:author_username>", blog_views, name='author'),
    path('search/',blog_search_views, name='blog-search'),
]