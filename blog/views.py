from django.shortcuts import render

# Create your views here.
def blog_views(request):
    return render(request,'blog/blog.html')

def blog_details_views(request):
    return render(request,'blog/details.html')