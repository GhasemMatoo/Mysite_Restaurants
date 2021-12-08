from django import template
from blog.models import post
from blog.models import Category

##------------------------------
register = template.Library()


@register.inclusion_tag('blog/side_bar/blog-box-post.html')
def Recent_Post():
    postes = post.objects.filter(status=1).order_by('published_date')[:4]
    return {'postes':postes} 

@register.inclusion_tag('blog/side_bar/blog-categories.html')
def Categories_Post():
    postes = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name]=postes.filter(category=name).count()
    return {'categories':cat_dict}

