from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import post,Category,comment
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_filter = ('status','name','category','author__username')
    list_display =('title','author','name','countent_views','status','published_date','id')
    search_fields = ('title', 'author__username')


class commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_dispyley = '-empty-'
    list_display = ('name','email', 'approved', 'created_date')
    list_filter = ('messages','subject')
    search_fields = ('name', 'messages')

admin.site.register(comment,commentadmin)
admin.site.register(Category)
admin.site.register(post,PostAdmin)
