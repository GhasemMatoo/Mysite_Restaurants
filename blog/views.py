from django.shortcuts import render, get_object_or_404
from blog.models import post, comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.Form import commentForm
from django.contrib import messages
from taggit.models import Tag

# Create your views here.


def blog_views(request, **kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs.get('cat_name'))
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs.get('author_username'))
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs.get('tag_name')])

    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    tags = Tag.objects.all()
    contex = {'posts': posts, 'Tags':tags}
    return render(request, 'blog/blog.html', contex)


def blog_details_views(request, pid):
    Post_singl = get_object_or_404(post, id=pid, status=1)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.Poost_id = pid
            comments.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Yor Commets submited successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Yor Commets dident submited.')
    form = commentForm
    Post_singl.countent_views =Post_singl.countent_views + 1
    Post_singl.save()
    comments = comment.objects.filter(Poost=Post_singl.id, approved=True)
    contex = {'Post_singl': Post_singl, 'comments': comments, 'form': form}
    return render(request, 'blog/details.html', contex)


def blog_search_views(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        Ps = posts.filter(content__contains=request.GET.get('s'))
        if(len(Ps) == 0):
            Ps = posts.filter(title__contains=request.GET.get('s'))
        if(len(Ps) == 0):
            Ps = posts.filter(category__name__contains=request.GET.get('s'))
        posts = Ps
    contex = {'posts': posts}
    return render(request, 'blog/blog.html', contex)
