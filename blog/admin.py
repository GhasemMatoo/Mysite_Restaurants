from django.contrib import admin
from blog.models import post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    data_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_filter = ('status','name','category')
    list_display =('title','name','countent_views','status','published_date','id')
    search_fields =('titel',)
admin.site.register(Category)
admin.site.register(post,PostAdmin)
