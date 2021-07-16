from django.shortcuts import render,get_object_or_404
from blog.models import post
# Create your views here.
def blog_views(request,cat_name=None):
    posts= post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
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