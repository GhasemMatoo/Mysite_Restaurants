from django import template
from blog.models import post

##------------------------------
register = template.Library()

@register.inclusion_tag('mysit/sit/menu-box-post.html')
def Menu_Post():
    postes = post.objects.filter(status=1)
    return {'postes':postes} 
