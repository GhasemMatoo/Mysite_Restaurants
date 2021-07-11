from django.contrib import admin
from mysit.models import contact
# Register your models here.
class mysitAdmin(admin.ModelAdmin):
    data_hierarchy ='created_date'
    empty_value_display = '-empty-'
    list_filter = ('subject',)
    list_display =('name','subject','created_date')
    search_fields =['subject','email']

admin.site.register(contact)