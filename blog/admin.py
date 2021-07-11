from django.contrib import admin
from blog.models import post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    data_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_filter = ('status',)
    list_display =('title','countent_views','status','published_date')
    search_fields =['titel','content']
admin.site.register(post,PostAdmin)