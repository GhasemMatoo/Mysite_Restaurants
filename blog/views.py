from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def blog_views(request,cat_name=None):
    posts= post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    
    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    contex={'posts':posts}
    return render(request,'blog/blog.html',contex)

def blog_details_views(request,pid):
    Post_singl= get_object_or_404(post,id=pid,status=1)
    contex={'Post_singl':Post_singl}
    return render(request,'blog/details.html',contex)

def blog_search_views(request):
    posts= post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    contex={'posts':posts}
    return render(request,'blog/blog.html',contex)