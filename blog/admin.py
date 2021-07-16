from django.contrib import admin
from blog.models import post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_filter = ('status','name','category','author__username')
    list_display =('title','author','name','countent_views','status','published_date','id')
    search_fields = ('title', 'author__username')
admin.site.register(Category)
admin.site.register(post,PostAdmin)
